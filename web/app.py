from flask import Flask, render_template, request, redirect, url_for
import random

from challenge.challenge import Challenge

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
    challenge = Challenge(palavra_aleatoria, palavra_aleatoria)
    print(challenge.get_challenge())
    return render_template("index.html", challenge_view=challenge.get_challenge())

@app.route("/resultado", methods=["POST"])
def resultado():
    palavra_digitada = request.form["palavra"]
    palavra_aleatoria = request.form["palavra_aleatoria"]
    if palavra_digitada == palavra_aleatoria:
        return render_template("resultado.html", acerto=True)
    else:
        return render_template("resultado.html", acerto=False, challenge_view=palavra_aleatoria)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
