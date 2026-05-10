from flask import render_template, request, redirect, url_for
from app import app
from conexao import conexao


@app.route('/')
def Index():
    conn = conexao()
    cursor = conn.cursor()

    meta = cursor.execute(
        'SELECT COALESCE(valor_meta, 0) FROM meta').fetchone()
    lucro = cursor.execute(
        'SELECT COALESCE(SUM(valor_lucro),0) FROM lucro').fetchone()

    return render_template('index.html', meta=f'{meta[0]:.2f}', lucro=f'{lucro[0]:.2f}')


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
