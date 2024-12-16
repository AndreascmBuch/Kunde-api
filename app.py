import sqlite3
from flask import Flask, jsonify, request
from dotenv import load_dotenv # import fra .env fil
import os
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Load environment variables fra .env filen
load_dotenv()
db_path=os.getenv("db_path", "kunde_database.db")

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

# Configure JWT settings
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key
app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Ensure tokens are in headers
app.config['JWT_HEADER_NAME'] = 'Authorization'  # Default header name for JWT
app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Prefix for the token (e.g., Bearer <token>)

# Initialize the JWT manager
jwt = JWTManager(app)

# Ensure the database and 'kunder' table exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kunder (
            kunde_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            adress VARCHAR(255),
            contact VARCHAR(100),
            betaling INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Call this function at the start of the application
init_db()

@app.route('/debug', methods=['GET'])
def debug():
    return jsonify({
        "JWT_SECRET_KEY": app.config['JWT_SECRET_KEY'],
        "Database_Path": db_path
    }), 200

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
@jwt_required()
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
@jwt_required()
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
@jwt_required()
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
    app.run(debug=True)