from django.db import models


class Servico(models.Model):
    """Um tipo de serviço de montagem oferecido (ex.: guarda-roupa, cozinha)."""

    titulo = models.CharField(max_length=80)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordem", "id"]
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.titulo


class Projeto(models.Model):
    """Um móvel já montado, exibido na galeria do portfólio."""

    titulo = models.CharField(max_length=80)
    tipo_movel = models.CharField("Tipo de móvel", max_length=60)
    bairro = models.CharField("Bairro / cidade", max_length=60)
    cor_hex_inicio = models.CharField(
        "Cor inicial (hex)", max_length=7, default="#33475b",
        help_text="Usada no gradiente do card enquanto não há foto real.",
    )
    cor_hex_fim = models.CharField(
        "Cor final (hex)", max_length=7, default="#1f2328",
    )
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordem", "-id"]
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return f"{self.titulo} — {self.tipo_movel}"


class Depoimento(models.Model):
    """Avaliação de um cliente atendido."""

    nome = models.CharField(max_length=80)
    cidade = models.CharField(max_length=80)
    texto = models.TextField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return f"{self.nome} ({self.cidade})"


class SolicitacaoOrcamento(models.Model):
    """Pedido de orçamento enviado pelo formulário de contato."""

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    tipo_servico = models.CharField(max_length=100, blank=True)
    mensagem = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Solicitação de orçamento"
        verbose_name_plural = "Solicitações de orçamento"

    def __str__(self):
        return f"{self.nome} — {self.criado_em:%d/%m/%Y}"
