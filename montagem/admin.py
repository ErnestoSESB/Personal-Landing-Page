from django.contrib import admin

from .models import Depoimento, Projeto, Servico, SolicitacaoOrcamento


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ordem")
    ordering = ("ordem",)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo_movel", "bairro", "ordem")
    ordering = ("ordem",)


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "ativo")
    list_filter = ("ativo",)


@admin.register(SolicitacaoOrcamento)
class SolicitacaoOrcamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "tipo_servico", "criado_em")
    readonly_fields = ("criado_em",)
