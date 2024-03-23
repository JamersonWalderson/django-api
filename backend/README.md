# django-api

Projeto criado com base no vídeo 'COMO CRIAR UMA API REST DO ZERO COM DJANGO REST FRAMEWORK' do canal Pedro Impulcetto

## Como instalar
- git clone https://github.com/JamersonWalderson/django-api-books.git
- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- Acesse para conseguir o token: localhost:8000/api/token/
- Acesse para listar os livros localhost:8000/books/
- Para aumentar ou diminuir o tempo de vida do token acesse settings.py e configure ACCESS_TOKEN_LIFETIME
