from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

Senha_correta = 'gui'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        senha = request.form['senha']
        if senha == Senha_correta:
            return redirect(url_for('pagina_secreta'))
        else:
            error = 'Senha incorreta. Tente novamente.'
            print('Erro: Senha incorreta!')
    
    return render_template('index.html', mensagem=error)

@app.route('/pagina_secreta')
def pagina_secreta():
    return 'Você está na página secreta!'

if __name__ == '__main__':
    app.run(debug=True)
