from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import db, Transacao, Categoria

@app.route('/')
def index():
    #busca todas as transações
    transacoes = Transacao.query.all()
    return render_template('index.html', transacoes=transacoes)

@app.route('/receita', methods=['GET', 'POST'])
def adicionar_receita():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        data = request.form.get('data')
        valor_digitado = request.form.get('valor')
        valor_formatado = valor_digitado.replace('.', '').replace(',', '.')
        valor = float(valor_formatado)

        # Proteção: Garante que exista pelo menos uma categoria no banco
        categoria = Categoria.query.filter_by(tipo="Receita").first()
        if not categoria:
            categoria = Categoria(nome="Geral Receita", tipo="Receita")
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
        
    return render_template('form.html', titulo="Cadastrar Receita", cor="primary", rota="adicionar_receita")

@app.route('/despesa', methods=['GET', 'POST'])
def adicionar_despesa():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        data = request.form.get('data')
        valor_digitado = request.form.get('valor')
        valor_formatado = valor_digitado.replace('.', '').replace(',', '.')
        valor = float(valor_formatado)

        # Proteção: Garante que exista pelo menos uma categoria no banco
        categoria = Categoria.query.filter_by(tipo="despesa").first()
        if not categoria:
            categoria = Categoria(nome="Geral Despesa", tipo="Despesa")
            db.session.add(categoria)
            db.session.commit()

        nova_despesa = Transacao(
            descricao=descricao, 
            valor=valor, 
            data=data, 
            categoria_id=categoria.id
        )

        db.session.add(nova_despesa)
        db.session.commit()

        flash('Despesa cadastrada com sucesso!', 'success')

        return redirect(url_for('index'))
    
    return render_template('form.html', titulo="Cadastrar Despesa", cor="danger", rota="adicionar_despesa")

@app.route('/editar/<int:id_transacao>', methods=['GET', 'POST'])
def editar(id_transacao):
    transacao = Transacao.query.get_or_404(id_transacao)
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        data = request.form.get('data')

        valor_digitado = request.form.get('valor')
        valor_formatado = valor_digitado.replace('.', '').replace(',', '.')
        valor = float(valor_formatado)

        transacao.descricao = descricao
        transacao.valor = valor
        transacao.data = data

        db.session.commit()

        flash('Receita alterada com sucesso!', 'success')
        return redirect(url_for('index'))

    if transacao.categoria.tipo == 'Receita':
        titulo_form = "Editar Receita"
        cor_form = "primary"
    else:
        titulo_form = "Editar Despesa"
        cor_form = "danger"
    
    return render_template('form.html', titulo=titulo_form, cor=cor_form, transacao=transacao)

@app.route('/deletar/<int:id_transacao>')
def deletar(id_transacao):
    transacao = Transacao.query.get_or_404(id_transacao)
    db.session.delete(transacao)
    db.session.commit()

    flash('Transação deletada com sucesso!', 'success')
    return redirect(url_for('index'))