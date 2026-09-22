from django import forms

from .models import SolicitacaoOrcamento


class SolicitacaoOrcamentoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoOrcamento
        fields = ["nome", "telefone", "tipo_servico", "mensagem"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Seu nome"}),
            "telefone": forms.TextInput(attrs={"placeholder": "WhatsApp com DDD"}),
            "tipo_servico": forms.TextInput(attrs={"placeholder": "Ex.: guarda-roupa 3 portas"}),
            "mensagem": forms.Textarea(attrs={"placeholder": "Endereço, prazo e detalhes do móvel", "rows": 4}),
        }
        labels = {
            "nome": "Nome",
            "telefone": "Telefone",
            "tipo_servico": "O que precisa montar?",
            "mensagem": "Mensagem",
        }
