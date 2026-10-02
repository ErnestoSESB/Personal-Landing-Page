from django.contrib import admin

from .models import Depoimento, Projeto, Servico, SolicitacaoOrcamento, VisitaSite


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ordem")
    ordering = ("ordem",)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo_movel", "bairro", "ordem")
    list_editable = ("ordem",)
    ordering = ("ordem",)
    search_fields = ("titulo", "tipo_movel", "bairro")
    list_per_page = 25


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "ativo")
    list_filter = ("ativo",)


@admin.register(VisitaSite)
class VisitaSiteAdmin(admin.ModelAdmin):
    list_display = ("criado_em", "path", "ip")
    list_filter = ("criado_em",)
    date_hierarchy = "criado_em"
    readonly_fields = ("criado_em", "path", "ip", "user_agent")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(SolicitacaoOrcamento)
class SolicitacaoOrcamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "tipo_servico", "criado_em")
    readonly_fields = ("criado_em",)
