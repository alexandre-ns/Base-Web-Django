# Basic website post(EM FASE DE TESTES E CORREÇÕES)
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/alexandre-ns/Base-Web-Django/blob/main/LICENSE) 

# Sobre projeto Basic website post

"Basic website post" é uma aplicação full stack web criada com Django/bootstrap. O objetivo dessa aplicação é servir como base para projetos web que realizem postagens de texto. Ao rodar a aplicação temos acessivel tanto o web site, quanto o painel de administração django(django admin) lugar onde é possivel gerenciar o contúdo do site assim como parte da aparência.

# Funcionamento

Após iniciar a aplicação temos o ambiente de adminstração django, que é onde podemos iniciar a montagem do website.
## Django Admin
![admin 1](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/admin01.png)


### CONTATO E MIDIAS SOCIAIS
![admin 1](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/admin04.png)

- Mensagens - Parte onde são exibidas as mensagens enviadas por usuários do website através da página de contato.

- Redes Sociais - Criar links para redes sociais que serão exibidas como icones na parte inferior de cada página - X(Twitter), Instagram, Facebook, GitHub

### PUBLICAÇÕES
![admin 2](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/admin03.png)

 - Fontes - Fontes que formarão o conteúdo, sendo exibidas no final de cada publicação.
    - 'Ordem do texto' - Campo que define a ordem que os textos serão exibidas em uma publicação.

- Textos - Textos que formarão o conteúdo da publicação.
    - 'Ordem do texto' - Campo que define a ordem que os textos serão exibidas em uma publicação.

- Publicações - Lugar indicado para criação de novas postagens, permitindo criar publicações, textos e fontes em um único lugar.

### WEB SITE(**OBRIGATÓRIO)
![admin 2](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/admin02.png)

##### Para o Correto funcionamento cada modelo de página deve possuir um e somente um elemento com campo 'Página ativa' ativado.
- Página Contatos - Construção de tela da página CONTATO 
- Página Sobre - Construção de tela da página SOBRE.
- Página Inicial - Construção de tela da página INICIAL.

### Exemplo simples de resultado de Layout web
![site 5](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/site07.png)

Página Inicial.

![site 6](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/site06.png)

Página Contato.

![site 6](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/site03.png)
![site 6](https://github.com/alexandre-ns/Assets/blob/main/basic_web_blog/site04.png)

Redes sociais


## Tecnologias utilizadas
- Python
- Django

- HTML
- CSS
- JavaScript
- *Bootstrap


# Como executar o projeto

Pré-requisitos: 
    - Python
    - Django
    - pip
    - Ambiente virtual python(opcional, mas recomendado)

## Ambiente de produção.
1. Configurar Variáveis de Ambiente.
    - SECRET_KEY

3. Configurações variáveis de Segurança.
    - DEBUG
    - ALLOWED_HOSTS
    - SECURE_SSL_REDIRECT
    - SECURE_HSTS_SECONDS
    - SECURE_HSTS_INCLUDE_SUBDOMAINS
      
4. Configuração de arquivos estáticos e media.
    - STATIC_ROOT
    - STATIC_URL
    - MEDIA_ROOT
    - MEDIA_URL
  
5. Definição de logging para monitoramento de atividades e erros.

6. Configuração de Banco de dados.
    - DATABASES

7. Instalação/Configuração um servidor de aplicação.(como Gunicorn ou uWSGI)

8. Instalação/configuração de servidor WEB(como Nginx ou Apache)

9. Configuração HTTPS.
    - SSL(Encrypt)
    - HTTPS <-> Nginx(Certbot)

### Ambiente de desenvolvimento.
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

# Autor

Alexandre Nogueira.

https://www.linkedin.com/in/alexandre-nogueira-4b2329a6/
