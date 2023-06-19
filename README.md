# API REGISTER EMPLOYEE

Bem-vindo(a) à API register employee! Esta API foi desenvolvida em Python e Django para fornecer um sistema capaz 
de gerenciar funcionários e consultas.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Python 3.10 ou superior

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/api-exemplo.git
   cd api-exemplo
   pip install -r requirements.txt

2. Crie e configure um aquivo `.env` com as informações necessárias. Você pode se basear no arquivo 
.env.example fornecido. 

3. Criação e configuração:
    ```bash
    python manage.py migrate
    python manage.py runserver

4. Agora a api estará disponível em http://localhost:8000/

## ROTAS

### Employee
✅ GET /employee/all/: Retorna todos os funcionários cadastrados.

✅ GET /employee/all/: Retorna todos os funcionários cadastrados.

✅ GET /employee/{employee_id}/: Retorna os detalhes de um funcionário específico.

✅ POST /employee/create/: Cria um novo funcionário. (requer autenticação)

### Query
✅ GET /query/all/: Retorna todas as consultas cadastradas.

✅ POST /query/create/: Cria uma nova consulta. (requer autenticação)

✅ POST /query/consult/: Consulta uma consulta pelo nome do funcionário.