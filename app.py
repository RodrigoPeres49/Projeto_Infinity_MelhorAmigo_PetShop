from flask import Flask, render_template, redirect

# IMPORTAÇÕES DAS ROTAS

from routes.produtos import produtos
from routes.lojas import lojas
from routes.mensagens import email_bp
from routes.outros import outros


# DEFINIÇÃO DO APLICATIVO

app = Flask(__name__)
app.secret_key='123'

# ROTAS DO BLUEPRINT

app.register_blueprint(produtos)
app.register_blueprint(lojas)
app.register_blueprint(email_bp)
app.register_blueprint(outros)

# ROTAS PRINCIPAIS

@app.route('/')
def index():
    return redirect('/sobre')

@app.route('/sobre')
def sobre():
    return render_template("melhoramigo/main/inicial.html")

# EXECUÇÃO DO APLICATIVO

if __name__ == "__main__":
    app.run(debug=True)