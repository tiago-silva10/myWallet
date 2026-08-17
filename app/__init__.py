from flask import Flask
from app.models import db


# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configuração essencial para o Flask e para o Flash
app.config['SECRET_KEY'] = 'minha_chave_super_secreta'

# CONFIGURAÇÃO DO BANCO DE DADOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mywallet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Conecta o banco ao app
db.init_app(app)

from app import controllers # Importamos as rotas (controllers)

