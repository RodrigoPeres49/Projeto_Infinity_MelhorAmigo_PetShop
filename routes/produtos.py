from flask import render_template, Blueprint

produtos = Blueprint('produtos', __name__)

@produtos.route('/produtos/caes')
def produtos_caes():

    return render_template("melhoramigo/main/produtos/produtos_caes.html")

@produtos.route('/produtos/gatos')
def produtos_gatos():

    return render_template("melhoramigo/main/produtos/produtos_gatos.html")

@produtos.route('/produtos/outros')
def produtos_outros():

    return render_template("melhoramigo/main/produtos/produtos_outros.html")

@produtos.route('/produtos/kits')
def produtos_kits():

    return render_template("melhoramigo/main/produtos/kits.html")

@produtos.route('/produtos/ofertas')
def produtos_ofertas():

    return render_template("melhoramigo/main/produtos/ofertas.html")