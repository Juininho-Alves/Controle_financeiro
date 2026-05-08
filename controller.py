from flask import render_template, request, redirect, url_for
from app import app


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/cadastro')
def Cadastro():
    return render_template('cadastro.html')
