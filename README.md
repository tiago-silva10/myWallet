# 💰 MyWallet - Gerenciador Financeiro Pessoal

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

Um aplicativo web simples e eficiente para gerenciamento de finanças pessoais. Desenvolvido para aplicar e demonstrar conceitos práticos de desenvolvimento web utilizando a stack **Python + Flask + MySQL**, estruturado no padrão **MVC (Model-View-Controller)**.

## 🎯 Funcionalidades

* **Dashboard Interativo:** Visão geral rápida do saldo atual, total de receitas e total de despesas.
* **Gestão de Transações:** Cadastro, edição, exclusão e listagem (CRUD) de receitas e despesas.
* **Categorização:** Classificação de transações por categorias personalizadas (ex: Alimentação, Moradia, Salário).
* **Feedback Visual (UX):** Tratamento de erros e mensagens de sucesso utilizando `Flask-Flash`.
* **Banco de Dados Relacional:** Controle de persistência de dados utilizando o ORM SQLAlchemy com MySQL.

## 📐 Arquitetura do Projeto (MVC)

O projeto foi organizado visando a separação de responsabilidades (Separation of Concerns), facilitando a manutenção e escalabilidade:

* **Model (`models.py`):** Mapeamento Objeto-Relacional (ORM) das entidades de banco de dados (Transações, Categorias).
* **View (`templates/`):** Interface do usuário em HTML renderizada dinamicamente com Jinja2 e estilizada com Bootstrap.
* **Controller (`controllers.py`):** Lógica de negócios e gerenciamento de rotas.

## 📁 Estrutura de Diretórios

```text
mywallet/
├── app/
│   ├── __init__.py          # Inicialização do app, banco de dados e configurações
│   ├── models.py            # Definição das classes do banco de dados (Model)
│   ├── controllers.py       # Rotas e regras de negócio (Controller)
│   └── templates/           # Arquivos HTML Jinja2 (View)
│       ├── base.html        
│       ├── index.html       
│       └── form.html        
├── .env.example             # Exemplo de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
├── config.py                # Configurações dinâmicas baseadas no .env
├── requirements.txt         # Dependências do projeto
└── run.py                   # Script de execução
