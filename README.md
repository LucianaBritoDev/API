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
  "image_url": "https://www.amazon.com.br/C%C3%B3digo-limpo-Robert-C-Martin/dp/8576082675/ref=sr_1_5?crid=1Q9YJ2PDGQCUB&dib=eyJ2IjoiMSJ9.LWKFR6v6o5UJzzTXfiQSfeFyGj95n3RapxBRarYa_UgEEC_JWIHZpAOU9MnjSp5GaSkeviKI3AIthfDNk0mo9_72tunqefLBkX00X_V6AdI65AaMV3dDQ0JFX-EBjl978SkiRbAOzHEpxOwABMS_km6x83xopX0zdeUxyQFLC-yJPhFR4N4O3_U6H-4P8L9Jitu1rMukDFEKKxa-T56ZfEKbh0kDpz38Ubv89c3L1_TWAbcqxq3TugnE40QDqkfFKPI6KfvyQW0rTwyv-u9DXVu-XdCicqGIIvYTHbIZIS-2cBTUZk8Doz5x8k33BntpCXoI331S6O5kdvTi_xuDybxn0V0trQEtfrnuHaFfmeq4H86eOjkjs4cVoUEEq_URDSDhrqdbbtRbAf7aha-vpcP9HEnyPZypfBIQTGgKAy8Lv9FvJ06EBKeAMaH12SIU.n2xOws6ggkAPV6bBDtXypnS_Tdk9ZRftMZKSxacGAN4&dib_tag=se&keywords=livros+sobre+programa%C3%A7%C3%A3o&qid=1742433109&sprefix=livros+sobre+pro%2Caps%2C259&sr=8-5&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9#detailBullets_feature_div"
}
```
