import sqlite3

# Opret forbindelse til database
conn = sqlite3.connect("kunde_database.db")
cursor = conn.cursor()

# Opret tabellerne
cursor.execute('''
CREATE TABLE IF NOT EXISTS kunder(
    kunde_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    adress VARCHAR(255),
    contact VARCHAR(100),
    betaling INTEGER         
)
''')

conn.commit()
conn.close()

