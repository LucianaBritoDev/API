from flask import Flask

app = Flask(__name__)

@app.route("/pagar")
def exibir_mensagem():
  return "<h1>Pagar as pessoas, faz bem!</h1>"

@app.route("/fernandadopix")
def manda_o_pix():
  return "<h1>Se a tela apagou, tá devendo!</h1>"

@app.route("/comida")
def comida():
   return "<h2>Tomtato à milanesa</h2>"

# Se o arquivo app.py for o arquivo principal da nossa aplicação, rode a api no modo de depuração.

if __name__ == "__main__":
    app.run(debug=True)

app.run()
