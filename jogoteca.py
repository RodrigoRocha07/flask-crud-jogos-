from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        

jogos = []

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos = jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    return redirect('/')

@app.route('/deletar/<nome>')
def deletar(nome):
    for jogo in jogos:
        if jogo.nome == nome:
            jogos.remove(jogo)
            break
    return redirect('/')


app.run(debug=True)