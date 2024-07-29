from flask import render_template, Blueprint

outros = Blueprint('outros', __name__)

@outros.route('/outros/servicos')
def produtos_caes():

    return render_template("melhoramigo/main/outros/servicos.html")

@outros.route('/outros/adocao')
def produtos_gatos():

    return render_template("melhoramigo/main/outros/adocao.html")

