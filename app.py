# Importei a classe Flask do módulo flask para criar nosso aplicativo web.
from flask import Flask,request 

# Aqui criei uma instância do Flask e armazenando na variável "app".
# O parâmetro __name__ é passado para o Flask para que ele consiga identificar o arquivo principal da aplicação.

import sqlite3
app = Flask(__name__)

# Exemplo: foi criado uma rota para o endpoint "/comida".
# Sempre que o usuário acessar http://127.0.0.1:5000/comida, essa função será executada.
@app.route("/comida")
def comida():
    # Retorna um texto formatado em HTML com uma mensagem sobre comida.
    return "<h2>Risoto de camarão com bacon</h2>"


def init_db():
    # sqlite3 cria o arquivo database.db e se conecta com a variável conn (connection).
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS LIVROS(
      id INTEGER PRIMARY KEY AUTOINCREMENT, # Cada livro recebbe um ID único automaticamente.
      titulo TEXT  NOT NULL,                # O título do livro, obrigatório e armazenado como texto.
      categoria TEXT NOT NULL,              # A categoria do livro, obrigatório e armazenado como texto.
      autor TEXT NOT NULL,                  # Nome do autor do livro, obrigatório e armazenado como texto.
      imagem_url TEXT NOT NULL              # Link para imagem da capa do livro, obrigatório e armazenado como texto.      
      )
""")

# Chamei a função para inicializar o banco de dados quando o programa for executado.
init_db()

@app.route("/doar", methods =["POST"])
def doar():

    # Variável dados recebe a resposta do cliente em JSON.
    dados = request.get_json()

    titulo = dados.get("titulo")          # Obtém o título do livro.
    categoria = dados.get("categoria")    # Obtém a categoria do livro.
    autor = dados.get("autor")            # Obtém o nome do autor do livro.
    imagem_url = dados.get("imagem_url")  # Obtém a URL da imagem do livro.

    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400

# Aqui verifica-se se o script está sendo executado diretamente e não importado como módulo.
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração.
    # O modo debug faz com que as mudanças no código sejam aplicadas automaticamente, sem necessidade de reiniciar o servidor manualmente.
    app.run(debug=True)

