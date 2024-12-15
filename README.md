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

# Anvendelse
Når applikationen kører, kan du få adgang til følgende endpoints for at interagere med kundedatabasen.

### Endpoints
GET /
Returnerer generel information om tjenesten.

```bash
curl http://localhost:5000/
POST /adduser
```

Tilføjer en ny kunde til databasen. Kræver JSON-data:

```bash
{
  "name": "John Doe",
  "adress": "123 Main St",
  "contact": "john.doe@example.com",
  "betaling": 100
}
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "adress": "123 Main St", "contact": "john.doe@example.com", "betaling": 100}' http://localhost:5000/adduser
GET /customers
```

Henter en liste over alle kunder.

```bash
curl http://localhost:5000/customers
GET /customers/<kunde_id>
```

Henter en specifik kunde baseret på kunde_id.

```bash
curl http://localhost:5000/customers/1
DELETE /customers/<kunde_id>
```

```bash
curl -X DELETE http://localhost:5000/customers/1
```
Licens
MIT-licensen - se LICENSE.md for detaljer.
