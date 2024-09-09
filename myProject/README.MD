# Projeto de Estudo em Django

Este repositório é um projeto de estudo desenvolvido com Django para fins de aprendizado e prática. O objetivo é experimentar diferentes funcionalidades e boas práticas do framework Django.

## Estrutura do Projeto

- **DJANGO/**: Pasta principal do projeto.
  - **myApp/**: Aplicativo Django.
  - **myProject/**: Diretório principal do projeto Django.
    - **__pycache__/**: Pasta gerada automaticamente com arquivos compilados.
    - **myApp/**: Aplicativo Django (também presente fora do diretório principal).
    - **myProject/**:
      - **__init__.py**: Inicializador do módulo.
      - **asgi.py**: Configuração do ASGI.
      - **settings.py**: Configurações do Django.
      - **urls.py**: Configurações de URL.
      - **wsgi.py**: Configuração do WSGI.
  - **myVenv/**: Ambiente virtual do projeto.
  - **.gitignore**: Arquivo para ignorar arquivos e pastas específicos no Git.
  - **sqlite3**: Banco de dados SQLite (não incluído no controle de versão).
  - **manage.py**: Script de gerenciamento do Django.
  - **requirements.txt**: Lista de dependências do projeto.

## Pré-requisitos

Certifique-se de ter o Python e o Django instalados. Você pode instalar as dependências necessárias com o seguinte comando:

```bash
pip install -r requirements.txt