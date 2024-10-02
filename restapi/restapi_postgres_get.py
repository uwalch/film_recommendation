from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# PostgreSQL-Datenbankverbindung konfigurieren
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_PORT = "5432"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

@app.route('/api/table/<table_name>', methods=['GET'])
def get_table_data(table_name):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Dynamische Abfrage für die Tabelle
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        cur.execute(query)
        rows = cur.fetchall()

        # Spaltennamen erhalten
        colnames = [desc[0] for desc in cur.description]

        # Ergebnisse als Liste von Dictionaries zurückgeben
        results = [dict(zip(colnames, row)) for row in rows]

        cur.close()
        conn.close()

        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
