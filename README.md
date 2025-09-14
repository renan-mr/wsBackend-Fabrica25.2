# 🐶 API Dog - Gerenciador de Cães Favoritos

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-darkgreen.svg?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST%20Framework-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-316192.svg?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📌 Sobre o Projeto
Uma **API RESTful** construída com **Django** e **Django REST Framework** que consome a [dog.api](https://dog.ceo/dog-api/) para obter informações sobre raças de cães e permite que os usuários gerenciem uma lista local de **pessoas e seus cães favoritos**.

---

## 🚀 Funcionalidades
- 👤 **CRUD de Pessoas**: Crie, visualize, atualize e delete registros de pessoas.  
- 🐕 **CRUD de Cães Favoritos**: Associe cães favoritos a pessoas.  
- 🌐 **Integração Externa**: Endpoint para listar todas as raças diretamente da `dog.api`.  
- 💾 **Banco de Dados Robusto**: Utiliza **PostgreSQL**.  
- 🎯 **API Amigável**: Serializers customizados exibem o nome da pessoa associada ao cão favorito.  

---

## 🛠 Tecnologias Utilizadas
- Python 3.8+  
- Django  
- Django REST Framework  
- PostgreSQL  
- psycopg2-binary  

---

## ⚙️ Configuração do Ambiente Local

### 1. Pré-requisitos
- Python 3.8+  
- PostgreSQL rodando localmente  

### 2. Clone o Repositório
git clone https://github.com/renan-mr/wsBackend-Fabrica25.2  
cd Projeto_dog  

### 3. Crie e Ative o Ambiente Virtual
Windows:  
python -m venv venv  
venv\Scripts\activate  

Linux / macOS:  
python -m venv venv  
source venv/bin/activate  

### 4. Instale as Dependências
pip install -r requirements.txt  

### 5. Configure o Banco de Dados
Crie um banco de dados vazio no PostgreSQL (ex: api_dog_db).  
Edite o arquivo `.env` (ou `settings.py`) com suas credenciais:  

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'api_dog_db',  
        'USER': 'seu_usuario_postgres',  
        'PASSWORD': 'sua_senha_postgres',  
        'HOST': 'localhost',  
        'PORT': '5432',  
    }  
}  

### 6. Aplique as Migrações
python manage.py migrate  

### 7. Inicie o Servidor
python manage.py runserver  

A API estará disponível em:  
👉 http://127.0.0.1:8000/  

---

## 📡 Endpoints da API

Base URL:  
http://127.0.0.1:8000/api_dog/  

### 👤 Pessoas
- GET /pessoas/ → Lista todas as pessoas  
- POST /pessoas/ → Cria uma nova pessoa  
- GET /pessoas/{id}/ → Detalhes de uma pessoa  
- PUT /pessoas/{id}/ → Atualiza dados  
- DELETE /pessoas/{id}/ → Remove pessoa  

Exemplo de POST:  
{  
  "nome": "João da Silva",  
  "email": "joao.silva@example.com"  
}  

---

### 🐕 Cães Favoritos
- GET /favorites/ → Lista todos os cães favoritos  
- POST /favorites/ → Adiciona um cão favorito  
- GET /favorites/{id}/ → Detalhes de um cão favorito  
- PUT /favorites/{id}/ → Atualiza um cão favorito  
- DELETE /favorites/{id}/ → Remove cão favorito  

Exemplo de POST:  
{  
  "id_raca": "a82d1c6a-04b3-4b6a-9f0c-2b2a1c1d1e1f",  
  "nome": "Pug",  
  "descricao": "Uma raça muito dócil e companheira.",  
  "notas": "Pesquisar sobre cuidados com a respiração.",  
  "pessoa_id": 1  
}  

ℹ️ O campo pessoa_id deve conter o ID de uma pessoa já existente.  

---

### 🌐 Raças (API Externa)
- GET /raca/ → Lista todas as raças de cães disponíveis na dog.api  

---

