from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

palavras = ["banana", "casa", "gato", "mesa", "livro"]
frases = [
"O sol brilha forte",
"A chuva cai suavemente",
"As folhas dançam ao vento",
"Os pássaros cantam alegremente",
"O café exala seu aroma",
"A lua brilha no céu escuro",
"O mar sussurra segredos",
"As flores desabrocham na primavera",
"As estrelas pontilham o firmamento",
"O fogo crepita na lareira"
]

@app.route("/")
def home():
    palavra_aleatoria = random.choice(palavras)
    return render_template("index.html", palavra=palavra_aleatoria)

@app.route("/resultado", methods=["POST"])
def resultado():
    palavra_digitada = request.form["palavra"]
    palavra_aleatoria = request.form["palavra_aleatoria"]
    if palavra_digitada == palavra_aleatoria:
        return render_template("resultado.html", acerto=True)
    else:
        return render_template("resultado.html", acerto=False, palavra_aleatoria=palavra_aleatoria)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
