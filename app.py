import sqlite3
from flask import Flask, jsonify, request

def get_db_connection():
    conn = sqlite3.connect('kunde_database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)


@app.route('/ddd', methods=['POST'])
def add_user():
 # Parse JSON from the request body
    data = request.get_json()
    name = data.get('name')
    adress = data.get('adress')
    contact = data.get('contact')
    betaling = data.get('betaling')


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO kunder (name, adress, contact, betaling)
        VALUES (?, ?, ?, ?)
    ''', (name, adress, contact, betaling))
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully!"}), 201

if __name__ == '__main__':
    app.run()