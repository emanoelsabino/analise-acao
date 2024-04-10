from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from utils.utils import analisar, formata_periodo


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        methods = "POST"
        codigo_ticker = request.form['codigo_ticker']
        periodo = request.form['periodo']
        periodo_formatado = formata_periodo(periodo)
        try:
            resultado = analisar(codigo_ticker, periodo)
        except:
            print('erro')
            return redirect('/')
        return render_template('index.html', resultado=resultado, methods=methods, codigo_ticker=codigo_ticker, periodo_formatado=periodo_formatado)
    
    methods = "GET"
    codigo_ticker = "PETR4.SA"
    periodo = "6mo"
    resultado = analisar(codigo_ticker, periodo)
    return render_template('index.html', resultado=resultado, methods=methods)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
