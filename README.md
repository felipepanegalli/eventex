# Eventex
Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/felipepanegalli/eventex.svg?branch=master)](https://travis-ci.org/felipepanegalli/eventex)
[![Code Health](https://landscape.io/github/felipepanegalli/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/felipepanegalli/eventex/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.7 (python3 -m venv venv).
3. Ative o virtualenv.
4. Instale as dependências (pip install -r requirements.txt).
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:felipepanegalli/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=FALSE
5. Configure o serviço de email de produção.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```