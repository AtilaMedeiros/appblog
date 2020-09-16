---
# API Restful & React de um Blog
---

<h1>
    <img src="https://github.com/AtilaMedeiros/appblog/blob/master/gif/appblog.gif">
</h1>


# Indice

- [Sobre](#-sobre)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como baixar o projeto](#-como-baixar-o-projeto)

## 🔖&nbsp; Sobre


Aplicação full stack desenvolvida durante a realização do curso **Desenvolvimento web com Django, React** que simula um blog com controle de login, visando colocar em prática todo conteúdo estudado.

---

## 🚀 Tecnologias utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias

- [Python](https://python.org.br/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://django-rest-framework.org/)
- [JavaScript](https://nodejs.org/en/)
- [React](https://reactjs.org/)



---

## 🗂 Como baixar o projeto

```bash

    # Pré-Requisitos de Ambiente
    $ Sudo apt Python3
    $ Sudo apt Pip3
    $ Sudo apt install python3-tk 
    $ Sudo apt install npm
	$ Sudo apt install nodejs

    # Clonar o repositório
    $ git clone https://github.com/AtilaMedeiros/appblog.git

    # Backend

        # Entrar no diretório
        $ cd appblog/backend

        # Instalar as dependências
        $ pip install -r requirements.txt

        # Crie o banco e tabelas
        $ python3 manage.py migrate
        $ python3 manage.py makemigrations

        # Crie o usuário
        $ python3 manage.py createsuperuser

        # Iniciar o projeto
        $ python manage.py runserver

        # Clique no link abaixo:
        $ http://127.0.0.1:8000/admin

    # Frontend

        # Entrar no diretório
        $ cd appblog/frontend

        # Instalar as dependências
        $ npm install 	

        # Inicia o servidor
        $ npm start
``` 

---

Desenvolvido  por Átila Medeiros Lavor
