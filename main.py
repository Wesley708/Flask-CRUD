from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def check_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
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
