# Kunde Service
Dette repository indeholder en Flask-baseret Kunde Service, der giver medarbejdere mulighed for at administrere kundedata via et RESTful API. Tjenesten gør det muligt at tilføje, hente, opdatere og slette kunder fra en SQLite-database.

### Kom godt i gang
Følg disse trin for at få en kopi af projektet op at køre på din lokale maskine til udviklings- og testformål.

### Installation
Klon dette repository til din lokale maskine:

```bash
git clone <repository_url>
cd <repository_folder>
```

Installer de nødvendige Python-pakker:

```bash
 pip install flask
```

Initialiser databasen ved at køre følgende script:

```bash
python database.py
```

Start applikationen:

```bash
python app.py
```

# API Endpoints
## 1. Registrer en ny kunde
- **URL:**  `/adduser`
- **Method:** `POST`
- **Request Body: JSON**

```
{
  "name": "John Doe",
  "adress": "123 Main St",
  "contact": "john.doe@example.com",
  "betaling": 100
}
```
- **Response:**
**201 Created:** Kunde tilføjet succesfuldt
**400 Bad Request:** Manglende eller ugyldige data
  
## 2. Hent alle kunder
- **URL:** `/customers`
- **Method:** `GET`
- **Response:**

**200 OK:** Returnerer en liste over alle kunder
```
[
  {
    "kunde_id": 1,
    "name": "John Doe",
    "adress": "123 Main St",
    "contact": "john.doe@example.com",
    "betaling": 100
  }
]
```

## 3. Hent en specifik kunde
- **URL:** `/customers/<kunde_id>`
- **Method:** `GET`
- **Response:**

200 OK: Returnerer oplysninger om den ønskede kunde

```
{
  "kunde_id": 1,
  "name": "John Doe",
  "adress": "123 Main St",
  "contact": "john.doe@example.com",
  "betaling": 100
}
```

404 Not Found: Kunden findes ikke

## 4. Slet en kunde
- **URL:** `/customers/<kunde_id>`
- **Method:** `DELETE`
- **Response:**

200 OK: Kunde slettet succesfuldt
404 Not Found: Kunden findes ikke

### Bemærkninger
Databasen: Systemet bruger en SQLite-database (kunde_database.db). For produktionsbrug bør en mere skalerbar løsning overvejes.
Autorisering: Ingen autorisation er på nuværende tidspunkt implementeret. I en produktionsapplikation bør autentifikation som JWT overvejes.
Opdatering af kunder: Endpoints til opdatering af kundedata mangler og kan tilføjes efter behov.
Licens
MIT License
