# Importei a classe Flask do módulo flask para criar nosso aplicativo web
from flask import Flask,request, jsonify

# Aqui criei uma instância do Flask e armazenando na variável "app".
# O parâmetro __name__ é passado para o Flask para que ele consiga identificar o arquivo principal da aplicação.

import sqlite3
app = Flask(__name__)

@app.route("/")

def inicial():
    return "<h1> Sistemas de Livros da Escola Vai Na Web! <h1>"    

def init_db():
    # sqlite3 cria o arquivo database.db e se conecta com a variável conn (connection).
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS LIVROS(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT  NOT NULL,                
      categoria TEXT NOT NULL,              
      autor TEXT NOT NULL,                  
      image_url TEXT NOT NULL                     
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
    image_url = dados.get("image_url")    # Obtém a URL da imagem do livro.

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400

    with sqlite3.connect("database.db") as conn:

        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")             
        """)

    conn.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

# Aqui verifica-se se o script está sendo executado diretamente e não importado como módulo.

@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
            dicionario_livros = {
                "id":item[0],
                "titulo":item[1],
                "categoria":item[2],
                "autor":item[3],
                "image_url":item[4]
            }
            livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados)

if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração.
    # O modo debug faz com que as mudanças no código sejam aplicadas automaticamente, sem necessidade de reiniciar o servidor manualmente.
    app.run(debug=True)

