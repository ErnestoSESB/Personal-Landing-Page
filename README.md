# Site do Montador de Móveis (Django)

Portfólio para um montador de móveis autônomo, feito em Django. Serviços,
projetos e depoimentos ficam no banco de dados e são editáveis pelo painel
de administração — nada de texto fixo no template.

## Como rodar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate        # cria o banco e já popula com dados de exemplo
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` para o site e `http://127.0.0.1:8000/admin/`
para editar serviços, projetos e depoimentos.

## Estrutura

```
config/            configurações e URLs raiz do projeto
montagem/           app com o site
  models.py         Servico, Projeto, Depoimento, SolicitacaoOrcamento
  views.py          página inicial + formulário de orçamento
  forms.py          formulário de pedido de orçamento
  templates/        home.html
  static/           style.css
  migrations/       schema + dados de exemplo (0002_seed_data.py)
```

## Personalizar

- Troque nome, telefone, e-mail e área de atendimento em
  `montagem/templates/montagem/home.html`.
- Edite serviços, projetos e depoimentos pelo `/admin/` (ou direto na
  migração `0002_seed_data.py` antes do primeiro `migrate`).
- Os cards de projeto usam gradientes de cor no lugar de fotos reais — para
  usar fotos, adicione um `ImageField` ao modelo `Projeto`, configure
  `MEDIA_URL`/`MEDIA_ROOT` e troque a `<div class="swatch">` do template por
  uma tag `<img>`.
- Pedidos de orçamento enviados pelo formulário ficam salvos em
  `SolicitacaoOrcamento`, visíveis no `/admin/`. Para receber por e-mail
  também, configure `EMAIL_BACKEND` em `settings.py` e envie um e-mail na
  view `home` após `form.save()`.

## Antes de publicar

- Gere uma `SECRET_KEY` nova e mantenha-a fora do repositório.
- Defina `DEBUG = False` e ajuste `ALLOWED_HOSTS`.
- Rode `python manage.py collectstatic` e sirva os arquivos estáticos
  (ex.: WhiteNoise ou pelo servidor web).
