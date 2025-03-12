from flask import Flask  # Importamos a classe Flask do módulo flask para criar nosso aplicativo web

# Aqui estamos criando uma instância do Flask e armazenando na variável "app"
# O parâmetro __name__ é passado para o Flask para que ele consiga identificar o arquivo principal da aplicação
app = Flask(__name__)

# Aqui estamos criando uma rota para o endpoint "/pagar"
# Ou seja, quando acessarmos http://127.0.0.1:5000/pagar no navegador, a função abaixo será executada
@app.route("/pagar")
def exibir_mensagem():
    # Retorna um texto formatado em HTML para ser exibido na página da rota "/pagar"
    return "<h1>Pagar as pessoas, faz bem as pessoas!!!</h1>"

# Criamos outra rota para o endpoint "/femandaopix"
# Quando acessarmos http://127.0.0.1:5000/femandaopix, a função será chamada automaticamente
@app.route("/femandaopix")
def manda_o_pix():
    # Retorna um texto formatado em HTML que será exibido no navegador
    return "<h2>SE TEM DOR DE CUTUVELO, TÁ DEVENDO</h2>"

# Criamos uma terceira rota para o endpoint "/comida"
# Sempre que o usuário acessar http://127.0.0.1:5000/comida, essa função será executada
@app.route("/comida")
def comida():
    # Retorna um texto formatado em HTML com uma mensagem sobre comida
    return "<h2>Tomato à milanesa</h2>"

# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração
    # O modo debug faz com que as mudanças no código sejam aplicadas automaticamente, sem necessidade de reiniciar o servidor manualmente
    app.run(debug=True)
