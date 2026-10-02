"""Tags de template do painel administrativo."""
from datetime import timedelta

from django import template
from django.utils import timezone

from ..models import Projeto, SolicitacaoOrcamento, VisitaSite

register = template.Library()


@register.inclusion_tag("painel_acessos.html")
def painel_acessos():
    agora = timezone.now()
    inicio_hoje = agora - timedelta(hours=24)
    inicio_7d = agora - timedelta(days=7)
    inicio_30d = agora - timedelta(days=30)

    return {
        "total": VisitaSite.objects.count(),
        "hoje": VisitaSite.objects.filter(criado_em__gte=inicio_hoje).count(),
        "semana": VisitaSite.objects.filter(criado_em__gte=inicio_7d).count(),
        "mes": VisitaSite.objects.filter(criado_em__gte=inicio_30d).count(),
        "projetos": Projeto.objects.count(),
        "orcamentos": SolicitacaoOrcamento.objects.count(),
        "orcamentos_hoje": SolicitacaoOrcamento.objects.filter(
            criado_em__gte=inicio_hoje
        ).count(),
    }
