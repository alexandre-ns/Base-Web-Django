# Big Game Survey 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/alexandre-ns/Base-Web-Django/blob/main/LICENSE) 

# Sobre o projeto

https://wmazoni-sds1.netlify.app

simple project web é uma aplicação full stack web criada com Django/bootstrap. O objetivo dessa aplicação é servir como base para projetos web que realizem postagens de texto. Ao rodar a aplicação temos acessivel tanto o web site, quanto o painel de administração django(django admin) lugar onde é possivel gerenciar o contúdo do site assim como parte da aparencia.

# Funcionamento

Após iniciar a aplicação temos o ambiente de adminstração django:




## Layout mobile
![admin 1](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/admin01.png)

## Layout web
![Web 1](https://github.com/acenelio/assets/raw/main/sds1/web1.png)

![Web 2](https://github.com/acenelio/assets/raw/main/sds1/web2.png)

## Modelo conceitual
![Modelo Conceitual](https://github.com/acenelio/assets/raw/main/sds1/modelo-conceitual.png)

# Tecnologias utilizadas
- Python
- Django

- HTML
- CSS
- JavaScript

## Implantação em produção
- Back end: Heroku
- Front end web: Netlify
- Banco de dados: Postgresql

# Como executar o projeto

Pré-requisitos: 
    - Python 3.12
    - Django 5.0
    - pip

Ambiente de desenvolvimento.
```bash

# clonar repositório
git clone https://github.com/alexandre-ns/Base-Web-Django.git

# entrar na pasta do projeto back end
cd Base-Web-Django

# Instalação de dependências
pip install -r requirements.txt

# criação dos arquivos de migração
python manage.py makemigrations

# Aplicação de migrações
python manage.py migrate

# Inicia servidor Django
python manage.py runserver
```

Para uso em ambiente de produção instalar e configurar Servidor Web (Gunicorn, uWSGI, etc.)

# Autor

Alexandre Nogueira.

https://www.linkedin.com/in/alexandre-nogueira-4b2329a6/