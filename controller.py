from flask import render_template, request, redirect, url_for
from app import app
from conexao import conexao
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def Index():
    atual = datetime.now().strftime('%d/%m/%Y')
    conn = conexao()
    cursor = conn.cursor()
    total_lucro = cursor.execute('SELECT SUM(valor) FROM movimentacoes WHERE tipo = "lucro"').fetchone()
    dados = cursor.execute('SELECT * FROM movimentacoes').fetchall()

    msg = None

    meta = cursor.execute(
        'SELECT COALESCE(valor_meta, 0) FROM meta').fetchone()

    if request.method == 'POST':
        tipo_movimentacoes = request.form.get('tipo_movimentacoes')
        motivo = request.form.get('motivo')
        valor = request.form.get('valor')

        if tipo_movimentacoes == None:
            msg = 'Selecione o tipo de movimentação'

        elif all([tipo_movimentacoes, motivo, valor]):
            cursor.execute('INSERT INTO movimentacoes (tipo, motivo, dia, valor) VALUES (?,?,?,?)',
                           (tipo_movimentacoes, motivo, atual, valor))
            conn.commit()
            conn.close()
            return redirect(url_for('Index'))

    return render_template('index.html', meta=f'{meta[0]:.2f}', msg=msg, dados=dados,total_lucro=f'{total_lucro[0]:.2f}')


@app.route('/cadastro', methods=['GET', 'POST'])
def Cadastro():
    conn = conexao()
    cursor = conn.cursor()

    if request.method == 'POST':
        valor_meta = request.form.get('valor_meta')

        if valor_meta:
            cursor.execute('INSERT INTO META (valor_meta) VALUES (?)',
                           (valor_meta,))
            conn.commit()
            conn.close()
            return redirect(url_for('Index'))

    return render_template('cadastro.html')
