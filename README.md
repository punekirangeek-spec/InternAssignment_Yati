# Employee CRUD API

A REST API built with Python and Flask for managing employee data, backed by a PostgreSQL database.

---

## Project Overview

This project provides a simple REST API to perform Create, Read, Update, and Delete (CRUD) operations on employee records. It was built as part of an internship assignment using Flask, SQLAlchemy, and PostgreSQL.

### Employee fields:
- Employee ID (auto-generated)
- First Name
- Last Name
- Email
- Phone Number
- Department
- Designation
- Salary
- Joining Date

---

## Steps to Run the Project

### 1. Clone the repository
```
git clone https://github.com/punekirangeek-spec/InternAssignment_Yati
cd InternAssignment_Yati
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Set up the database
- Install PostgreSQL and open pgAdmin
- Create a new database called `employee_db`

### 4. Configure environment variables
Create a `.env` file in the project root with the following:
```
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=employee_db
```

### 5. Run the application
```
python app.py
```

The server will start at `http://127.0.0.1:5000`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| GET | `/employees/<id>` | Get a single employee by ID |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/<id>` | Update an existing employee |
| DELETE | `/employees/<id>` | Delete an employee |

### Example POST request body:
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@company.com",
    "phone": "9876543210",
    "department": "Engineering",
    "designation": "Software Engineer",
    "salary": 75000,
    "joining_date": "2024-01-15"
}
```

---

## Database

- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (via Flask-SQLAlchemy)
- **Table:** `employees`

The table is created automatically when the app runs for the first time.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| Flask | Web framework and API routing |
| Flask-SQLAlchemy | Database ORM for PostgreSQL |
| Flask-Marshmallow | JSON serialization and validation |
| marshmallow-sqlalchemy | Marshmallow integration with SQLAlchemy |
| psycopg2-binary | PostgreSQL driver for Python |
| python-dotenv | Loads environment variables from .env file |

Install all dependencies with:
```
pip install -r requirements.txt
```

---

## Project Structure

```
InternAssignment_Yati/
├── app.py              # Flask app and API routes
├── models.py           # Employee database model
├── schemas.py          # Marshmallow serialization schemas
├── config.py           # Database configuration
├── database.py         # SQLAlchemy instance
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (not committed)
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation
```
