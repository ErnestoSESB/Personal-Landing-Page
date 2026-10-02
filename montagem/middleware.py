"""Contagem de acessos ao site para exibir no painel administrativo."""
from django.utils import timezone

from .models import VisitaSite

CAMINHOS_IGNORADOS = ("/admin", "/static", "/media", "/favicon.ico")


def get_client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


class ContadorAcessosMiddleware:
    """Registra 1 acesso por sessão/hora (evita inflar o número ao recarregar)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self._registrar(request)
        return self.get_response(request)

    def _registrar(self, request):
        if request.method != "GET" or not request.path:
            return
        if any(request.path.startswith(p) for p in CAMINHOS_IGNORADOS):
            return

        hora_atual = timezone.now().strftime("%Y-%m-%d-%H")
        if request.session.get("acesso_registrado") == hora_atual:
            return
        request.session["acesso_registrado"] = hora_atual

        VisitaSite.objects.create(
            path=request.path[:200],
            ip=get_client_ip(request) or None,
            user_agent=request.META.get("HTTP_USER_AGENT", "")[:250],
        )
