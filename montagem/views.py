from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SolicitacaoOrcamentoForm
from .models import Depoimento, Projeto, Servico


def home(request):
    if request.method == "POST":
        form = SolicitacaoOrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Pedido recebido! Respondo pelo WhatsApp em até um dia útil.",
            )
            return redirect(f"{request.path}#contato")
    else:
        form = SolicitacaoOrcamentoForm()

    contexto = {
        "servicos": Servico.objects.all(),
        "projetos": Projeto.objects.all(),
        "depoimento": Depoimento.objects.filter(ativo=True).first(),
        "form": form,
    }
    return render(request, "montagem/home.html", contexto)
