# Sistema de Gestão de Assinaturas e Gastos Recorrentes - Backend

## Descrição

Este é o backend do MVP do Sistema de Gestão de Assinaturas e Gastos Recorrentes, desenvolvido como projeto de final de período da pós-graduação. O sistema oferece uma API REST completa para gerenciamento de usuários, assinaturas e gastos recorrentes, com documentação automática via OpenAPI/Swagger.

## Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** - Framework web para Python
- **Flask-OpenAPI3** - Integração do Flask com OpenAPI 3.0 para documentação automática
- **Pydantic** - Validação de dados e serialização
- **SQLAlchemy** - ORM para Python
- **SQLite** - Banco de dados relacional
- **Flask-CORS** - Suporte a Cross-Origin Resource Sharing

## Estrutura do Projeto

```
backend/subscription-manager/
├── src/
│   ├── models/                 # Modelos de dados SQLAlchemy
│   │   ├── user.py            # Modelo de usuário
│   │   ├── subscription.py    # Modelo de assinatura
│   │   └── recurring_expense.py # Modelo de gasto recorrente
│   ├── schemas/               # Schemas Pydantic para validação
│   │   ├── user_schemas.py    # Schemas de usuário
│   │   ├── subscription_schemas.py # Schemas de assinatura
│   │   └── recurring_expense_schemas.py # Schemas de gasto recorrente
│   ├── routes/                # Rotas da API
│   │   ├── user.py           # Rotas de usuários
│   │   ├── subscription.py   # Rotas de assinaturas
│   │   └── recurring_expense.py # Rotas de gastos recorrentes
│   ├── static/               # Arquivos estáticos do frontend
│   ├── database/             # Banco de dados SQLite
│   │   └── app.db           # Arquivo do banco de dados
│   └── main.py              # Arquivo principal da aplicação
├── venv/                    # Ambiente virtual Python
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## Funcionalidades

### API de Usuários
- **GET /api/users** - Listar todos os usuários
- **POST /api/users** - Criar novo usuário
- **GET /api/users/{user_id}** - Buscar usuário por ID
- **PUT /api/users/{user_id}** - Atualizar usuário
- **DELETE /api/users/{user_id}** - Deletar usuário

### API de Assinaturas
- **GET /api/subscriptions** - Listar todas as assinaturas
- **POST /api/subscriptions** - Criar nova assinatura
- **GET /api/subscriptions/{subscription_id}** - Buscar assinatura por ID
- **PUT /api/subscriptions/{subscription_id}** - Atualizar assinatura
- **DELETE /api/subscriptions/{subscription_id}** - Deletar assinatura
- **GET /api/users/{user_id}/subscriptions** - Listar assinaturas de um usuário

### API de Gastos Recorrentes
- **GET /api/recurring-expenses** - Listar todos os gastos recorrentes
- **POST /api/recurring-expenses** - Criar novo gasto recorrente
- **GET /api/recurring-expenses/{expense_id}** - Buscar gasto recorrente por ID
- **PUT /api/recurring-expenses/{expense_id}** - Atualizar gasto recorrente
- **DELETE /api/recurring-expenses/{expense_id}** - Deletar gasto recorrente
- **GET /api/users/{user_id}/recurring-expenses** - Listar gastos recorrentes de um usuário

## Instalação e Configuração

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório e navegue até o diretório do backend:**
   ```bash
   cd backend/subscription-manager
   ```

2. **Ative o ambiente virtual:**
   ```bash
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python src/main.py
   ```

A aplicação estará disponível em `http://localhost:5000`

## Comandos Úteis

### Desenvolvimento
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar nova dependência
pip install nome-do-pacote

# Atualizar requirements.txt
pip freeze > requirements.txt

# Executar aplicação em modo debug
python src/main.py
```

### Banco de Dados
O banco de dados SQLite é criado automaticamente na primeira execução da aplicação. O arquivo `app.db` fica localizado em `src/database/app.db`.

## Documentação da API

A documentação completa da API está disponível via Swagger UI quando a aplicação estiver rodando:

- **Swagger UI:** `http://localhost:5000/openapi/swagger`
- **OpenAPI JSON:** `http://localhost:5000/openapi/openapi.json`

## Modelos de Dados

### Usuário (User)
```python
{
    "id": int,
    "username": str,
    "email": str,
    "created_at": datetime
}
```

### Assinatura (Subscription)
```python
{
    "id": int,
    "name": str,
    "description": str (opcional),
    "price": float,
    "billing_cycle": str ("monthly", "yearly", "weekly"),
    "next_billing_date": date,
    "category": str (opcional),
    "is_active": bool,
    "user_id": int,
    "created_at": datetime,
    "updated_at": datetime
}
```

### Gasto Recorrente (RecurringExpense)
```python
{
    "id": int,
    "name": str,
    "description": str (opcional),
    "amount": float,
    "frequency": str ("daily", "weekly", "monthly", "yearly"),
    "next_due_date": date,
    "category": str (opcional),
    "is_active": bool,
    "user_id": int,
    "created_at": datetime,
    "updated_at": datetime
}
```

## Validação de Dados

O sistema utiliza Pydantic para validação automática de dados de entrada e saída. Todos os endpoints possuem validação rigorosa dos dados enviados, garantindo a integridade das informações.

### Exemplos de Validação

**Criação de Usuário:**
```json
{
    "username": "string (obrigatório)",
    "email": "email válido (obrigatório)"
}
```

**Criação de Assinatura:**
```json
{
    "name": "string (obrigatório)",
    "description": "string (opcional)",
    "price": "float (obrigatório)",
    "billing_cycle": "monthly|yearly|weekly (obrigatório)",
    "next_billing_date": "YYYY-MM-DD (obrigatório)",
    "category": "string (opcional)",
    "user_id": "int (obrigatório)"
}
```

## Tratamento de Erros

A API retorna códigos de status HTTP apropriados e mensagens de erro detalhadas:

- **200** - Sucesso
- **201** - Criado com sucesso
- **204** - Deletado com sucesso
- **400** - Erro de validação dos dados
- **404** - Recurso não encontrado
- **500** - Erro interno do servidor

## CORS (Cross-Origin Resource Sharing)

O backend está configurado para aceitar requisições de qualquer origem, permitindo a integração com o frontend desenvolvido separadamente.

## Segurança

### Considerações de Segurança Implementadas:
- Validação rigorosa de entrada de dados via Pydantic
- Sanitização automática de dados pelo SQLAlchemy
- Configuração adequada de CORS

## Testes

Para testar a API, você pode usar ferramentas como:

- **Swagger UI** (disponível em `/openapi/swagger`)
- **Postman** ou **Insomnia**
- **curl** via linha de comando

### Exemplo de Teste com curl:

```bash
# Criar usuário
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username": "teste", "email": "teste@email.com"}'

# Listar usuários
curl -X GET http://localhost:5000/api/users

# Criar assinatura
curl -X POST http://localhost:5000/api/subscriptions \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Netflix",
    "description": "Streaming de vídeos",
    "price": 29.90,
    "billing_cycle": "monthly",
    "next_billing_date": "2024-01-15",
    "category": "Entretenimento",
    "user_id": 1
  }'
```