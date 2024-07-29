from flask import render_template, Blueprint

lojas = Blueprint('lojas', __name__)

@lojas.route('/lojas/belohorizonte')
def cidade_belohorizonte():

    return render_template("melhoramigo/main/lojas/belohorizonte.html")

@lojas.route('/lojas/fortaleza')
def cidade_gatos():

    return render_template("melhoramigo/main/lojas/fortaleza.html")

@lojas.route('/lojas/recife')
def cidade_outros():

    return render_template("melhoramigo/main/lojas/recife.html")

@lojas.route('/lojas/salvador')
def cidade_kits():

    return render_template("melhoramigo/main/lojas/salvador.html")


