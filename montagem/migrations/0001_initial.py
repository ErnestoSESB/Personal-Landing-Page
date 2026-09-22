from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Servico",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=80)),
                ("descricao", models.TextField()),
                ("ordem", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Serviço",
                "verbose_name_plural": "Serviços",
                "ordering": ["ordem", "id"],
            },
        ),
        migrations.CreateModel(
            name="Projeto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=80)),
                ("tipo_movel", models.CharField(max_length=60, verbose_name="Tipo de móvel")),
                ("bairro", models.CharField(max_length=60, verbose_name="Bairro / cidade")),
                ("cor_hex_inicio", models.CharField(default="#33475b", max_length=7, verbose_name="Cor inicial (hex)", help_text="Usada no gradiente do card enquanto não há foto real.")),
                ("cor_hex_fim", models.CharField(default="#1f2328", max_length=7, verbose_name="Cor final (hex)")),
                ("ordem", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Projeto",
                "verbose_name_plural": "Projetos",
                "ordering": ["ordem", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Depoimento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=80)),
                ("cidade", models.CharField(max_length=80)),
                ("texto", models.TextField()),
                ("ativo", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Depoimento",
                "verbose_name_plural": "Depoimentos",
            },
        ),
        migrations.CreateModel(
            name="SolicitacaoOrcamento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=30)),
                ("tipo_servico", models.CharField(blank=True, max_length=100)),
                ("mensagem", models.TextField(blank=True)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Solicitação de orçamento",
                "verbose_name_plural": "Solicitações de orçamento",
                "ordering": ["-criado_em"],
            },
        ),
    ]
