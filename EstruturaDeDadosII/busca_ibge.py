from flask import Flask, request

app = Flask(__name__)


@app.route("/busca_nome")
def busca():
    try:
        var_nome = request.args.get("nome")
        return f"{var_nome}"
    except Exception as e:
        return "Falha na rota /busca_nome: {e}"
    pass


app.run(debug=True)