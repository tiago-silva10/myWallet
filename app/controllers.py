from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import db, Transacao, Categoria

@app.route('/')
def index():
    #busca todas as transações
    transacoes = Transacao.query.all()
    return render_template('index.html', transacoes=transacoes)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')
        data = request.form.get('data')

        # Proteção: Garante que exista pelo menos uma categoria no banco
        categoria = Categoria.query.first()
        if not categoria:
            categoria = Categoria(nome="Geral", tipo="Receita")
            db.session.add(categoria)
            db.session.commit()

        nova_transacao = Transacao(
            descricao=descricao, 
            valor=valor, 
            data=data, 
            categoria_id=categoria.id
        )

        db.session.add(nova_transacao)
        db.session.commit()

        flash('Receita cadastrada com sucesso!', 'success')

        return redirect(url_for('index'))
        
    return render_template('form.html')