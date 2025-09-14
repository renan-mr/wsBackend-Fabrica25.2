API Dog - Gerenciador de Cães Favoritos
Uma API RESTful construída com Django e Django REST Framework que consome a dog.api para obter informações sobre raças de cães e permite que os usuários gerenciem uma lista local de pessoas e seus cães favoritos.

Funcionalidades
CRUD de Pessoas: Crie, visualize, atualize e delete registros de pessoas.

CRUD de Cães Favoritos: Crie, visualize, atualize e delete registros de cães favoritos, associando cada um a uma pessoa.

Integração Externa: Endpoint para listar todas as raças de cães diretamente da dog.api.

Banco de Dados Robusto: Utiliza PostgreSQL para armazenamento de dados.

API Amigável: O serializer foi customizado para exibir o nome da pessoa associada ao cão favorito, em vez de apenas o seu ID.

Tecnologias Utilizadas
Python 3.8+

Django

Django REST Framework

PostgreSQL

psycopg2-binary

Configuração do Ambiente Local
Siga os passos abaixo para rodar o projeto na sua máquina.

1. Pré-requisitos
Python 3.8 ou superior instalado.

PostgreSQL instalado e rodando na sua máquina.

2. Clone o Repositório
git clone https://github.com/renan-mr/wsBackend-Fabrica25.2
cd Projeto_dog


3. Crie e Ative o Ambiente Virtual
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate


4. Instale as Dependências
Este projeto utiliza um arquivo requirements.txt para gerenciar as dependências.

pip install -r requirements.txt


5. Configure o Banco de Dados
a. Crie um banco de dados vazio no seu PostgreSQL (ex: api_dog_db).

b. Renomeie o arquivo .env.example para .env (ou configure diretamente o settings.py para desenvolvimento).

c. Edite o settings.py com as suas credenciais do PostgreSQL:

# Projeto_dog/settings.py

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


6. Aplique as Migrações
Este comando criará todas as tabelas necessárias no seu banco de dados.

python manage.py migrate


7. Inicie o Servidor
python manage.py runserver


A API estará disponível em http://127.0.0.1:8000/.

Como Usar a API (Endpoints)
A base de todas as URLs da API é http://127.0.0.1:8000/api_dog/.

Pessoas
GET /api_dog/pessoas/ - Lista todas as pessoas.

POST /api_dog/pessoas/ - Cria uma nova pessoa.

GET /api_dog/pessoas/{id}/ - Obtém detalhes de uma pessoa.

PUT /api_dog/pessoas/{id}/ - Atualiza os dados de uma pessoa.

DELETE /api_dog/pessoas/{id}/ - Deleta uma pessoa.

Exemplo de corpo (Body) para POST:

{
    "nome": "João da Silva",
    "email": "joao.silva@example.com"
}


Cães Favoritos
GET /api_dog/favorites/ - Lista todos os cães favoritos.

POST /api_dog/favorites/ - Adiciona um novo cão favorito.

GET /api_dog/favorites/{id}/ - Obtém detalhes de um favorito.

PUT /api_dog/favorites/{id}/ - Atualiza um favorito.

DELETE /api_dog/favorites/{id}/ - Deleta um favorito.

Exemplo de corpo (Body) para POST:

{
    "id_raca": "a82d1c6a-04b3-4b6a-9f0c-2b2a1c1d1e1f",
    "nome": "Pug",
    "descricao": "Uma raça muito dócil e companheira.",
    "notas": "Pesquisar sobre cuidados com a respiração.",
    "pessoa_id": 1
}


Nota: O campo pessoa_id deve conter o id de uma pessoa já existente no banco de dados.

Raças (API Externa)
GET /api_dog/raca/ - Lista todas as raças de cães disponíveis na dog.api.