from flask import Flask
import psycopg2
import os
from urllib.parse import urlparse

app = Flask(__name__)

def check_connection():
    try:
        # Obtendo a URL de conexão do Railway
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            return "Erro: DATABASE_URL não foi encontrada nas variáveis de ambiente."

        # Parseando a URL para extrair os dados
        result = urlparse(database_url)
        conn = psycopg2.connect(
            dbname=result.path[1:],
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
        conn.close()
        return "Conexão bem-sucedida!"
    except Exception as e:
        return f"Erro na conexão: {e}"

@app.route('/')
def index():
    return check_connection()

if __name__ == '__main__':
    app.run(debug=True)
