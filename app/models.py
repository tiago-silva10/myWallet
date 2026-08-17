from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)

    transacoes = db.relationship('Transacao', backref='categoria', lazy=True)

class Transacao(db.Model):
    __tablename__ = 'transacao'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    
    # Chave Estrangeira ligando com a tabela categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)

    def adicionar(descricao, valor, data):
        db = SQLAlchemy()
        SQLAlchemy = "INSERT INTO transacao (descricao, valor, data) VALUES (%s, %s, %s)"
        db.cursor.execute(SQLAlchemy, (descricao, valor, data))
        db.commit()
        


