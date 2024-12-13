import sqlite3
from flask import Flask, jsonify, request

def get_db_connection():
    conn = sqlite3.connect('kunde_database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

#Tilføj kunde
@app.route('/adduser', methods=['POST'])
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

#Hent alle kunder
@app.route('/customers', methods=['GET'])
def getall():
    conn = get_db_connection
    cursor = conn.cursor()
    cursor.exectute("SELECT * FROM kunder")
    kunder = cursor.fetchall()
    conn.close()
    return jsonify(kunder)

#Hent specifik kunde
@app.route('/customers/<int:kunde_id>', methods=['GET'])
def get_customer(kunde_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kunder WHERE kunde_id = ?", (kunde_id,))
    customer = cursor.fetchone()
    conn.close()
    return jsonify

#Rediger en kunde

#Slet en kunde
@app.route('/customers/<int:kunde_id>', methods=['DELETE'])
def delete(kunde_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kunder WHERE kunde_id = ?", (kunde_id,))
    conn.commit()
    conn.close()
    jsonify

# test route så vi ikke får 404
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Kunde Service",
        "version": "1.0.0",
        "description": "A RESTful API for managing customers"
    })


if __name__ == '__main__':
    app.run()