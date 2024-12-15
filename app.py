import sqlite3
from flask import Flask, jsonify, request
from dotenv import load_dotenv # import fra .env fil
import os

# Load environment variables fra .env filen
load_dotenv()
db_path=os.getenv("db_path", "user_database.db")

def get_db_connection():
    conn = sqlite3.connect('db_path')
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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kunder")
    kunder = cursor.fetchall()
    conn.close()
    kunder = [dict(row) for row in kunder]  # Convert each row to a dictionary
    return jsonify(kunder)

#Hent specifik kunde
@app.route('/customers/<int:kunde_id>', methods=['GET'])
def get_customer(kunde_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kunder WHERE kunde_id = ?", (kunde_id,))
    customer = cursor.fetchone()
    conn.close()
    if customer:
        return jsonify(dict(customer)), 200  # Convert the single row to a dictionary
    else:
        return jsonify({"message": "Customer not found"}), 404

#Rediger en kunde

#Slet en kunde
@app.route('/customers/<int:kunde_id>', methods=['DELETE'])
def delete(kunde_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kunder WHERE kunde_id = ?", (kunde_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Customer deleted successfully!"}), 200

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