from flask import Flask, render_template, request, redirect, url_for
import random
from icecream import ic

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
    challenge_answer = random.choice(palavras)
    challenge = Challenge(challenge_answer, challenge_answer)
    return render_template("index.html", challenge_view=challenge.get_challenge())

@app.route("/result", methods=["POST"])
def result():
    user_answer = request.form["user-answer"]
    challenge_answer = eval(request.form["challenge-answer"])[1]
    ic(user_answer, challenge_answer)

    if user_answer == challenge_answer:
        return render_template("result.html", acerto=True)
    else:
        return render_template("result.html", acerto=False, challenge_view=challenge_answer)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
