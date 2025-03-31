# API Livros Doados VnW

Essa é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai Na Web, ela permite cadastrar e listar os livros doados.

## Como rodar o projeto?

1. Faça o clone do repositório:

```bash
git clone <LINK_DO_REPOSITÓRIO>
cd nome_do_projeto
```

2. Criar um ambiente virtual (Obrigatório):

**Windows**

```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac**

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor:

```bash
python app.py
```

> A API estará disponível em http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoint para o cadastro das informações dos livros doados.

**Envio (JSON)**

```json
{
  "titulo": "Código Limpo: Habilidades Práticas do Agile Software",
  "categoria": "Computação",
  "autor": "Robert C. Martins",
  "image_url": "https://m.media-amazon.com/images/I/71dH97FwGbL._SY342_.jpg"
}
```
