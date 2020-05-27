from googletrans import Translator
from flask import Flask, request, render_template

translator = Translator()
app = Flask(__name__)

@app.route('/tradutor',methods=["POST"])
def main_tradutor():
    Texto_A_Traduzir = request.form["Traduzir"]
    idioma_origem = request.form["idioma"]
    idioma_destino =  request.form["idioma_destino"]
    result = translator.translate(Texto_A_Traduzir, src=idioma_origem, dest=idioma_destino)
    return render_template("index.html", mensagem=result.text)

@app.route("/tradutor")
def index_template():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port = 8080, debug = True)