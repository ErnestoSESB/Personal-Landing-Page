from django.db import migrations


def criar_dados_iniciais(apps, schema_editor):
    Servico = apps.get_model("montagem", "Servico")
    Projeto = apps.get_model("montagem", "Projeto")
    Depoimento = apps.get_model("montagem", "Depoimento")

    Servico.objects.bulk_create([
        Servico(
            titulo="Móveis planejados",
            descricao="Montagem de cozinhas, closets e home offices planejados, com nivelamento e ajuste fino de portas e gavetas.",
            ordem=1,
        ),
        Servico(
            titulo="Móveis de loja",
            descricao="Guarda-roupas, camas, estantes e racks comprados em caixa — de qualquer marca, com ou sem manual.",
            ordem=2,
        ),
        Servico(
            titulo="Fixação e instalação",
            descricao="Fixação de painéis de TV, prateleiras e armários na parede, com checagem de fiação e alvenaria.",
            ordem=3,
        ),
        Servico(
            titulo="Desmontagem para mudança",
            descricao="Desmontagem organizada antes da mudança e remontagem no novo endereço, com as peças identificadas.",
            ordem=4,
        ),
    ])

    Projeto.objects.bulk_create([
        Projeto(titulo="Cozinha planejada", tipo_movel="Cozinha completa", bairro="Pinheiros, São Paulo", cor_hex_inicio="#3d5166", cor_hex_fim="#1f2328", ordem=1),
        Projeto(titulo="Guarda-roupa 3 portas", tipo_movel="Guarda-roupa", bairro="Tatuapé, São Paulo", cor_hex_inicio="#4a6178", cor_hex_fim="#243040", ordem=2),
        Projeto(titulo="Home office completo", tipo_movel="Escrivaninha e estante", bairro="Vila Mariana, São Paulo", cor_hex_inicio="#c98a2c", cor_hex_fim="#7a5015", ordem=3),
        Projeto(titulo="Painel de TV suspenso", tipo_movel="Painel e rack", bairro="Moema, São Paulo", cor_hex_inicio="#33475b", cor_hex_fim="#141b22", ordem=4),
        Projeto(titulo="Closet sob medida", tipo_movel="Closet planejado", bairro="Perdizes, São Paulo", cor_hex_inicio="#5a4a78", cor_hex_fim="#241f33", ordem=5),
        Projeto(titulo="Beliche infantil", tipo_movel="Cama e escada", bairro="Santana, São Paulo", cor_hex_inicio="#3d6b5c", cor_hex_fim="#1c2e28", ordem=6),
    ])

    Depoimento.objects.create(
        nome="Camila R.",
        cidade="São Paulo",
        texto="Chegou no horário combinado, montou o guarda-roupa inteiro em duas horas e ainda alinhou as portas que já vinham tortas de fábrica.",
        ativo=True,
    )


def remover_dados_iniciais(apps, schema_editor):
    apps.get_model("montagem", "Servico").objects.all().delete()
    apps.get_model("montagem", "Projeto").objects.all().delete()
    apps.get_model("montagem", "Depoimento").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("montagem", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(criar_dados_iniciais, remover_dados_iniciais),
    ]
