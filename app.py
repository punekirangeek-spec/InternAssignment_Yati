from flask import Flask, request, jsonify
from config import Config
from database import db
from schemas import ma, employee_schema, employees_schema
from models import Employee

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

# Create all tables on startup
with app.app_context():
    db.create_all()


# ── CREATE ──────────────────────────────────────────────
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Check for duplicate email
    if Employee.query.filter_by(email=data.get('email')).first():
        return jsonify({'error': 'Email already exists'}), 409

    new_employee = Employee(
        first_name   = data.get('first_name'),
        last_name    = data.get('last_name'),
        email        = data.get('email'),
        phone        = data.get('phone'),
        department   = data.get('department'),
        designation  = data.get('designation'),
        salary       = data.get('salary'),
        joining_date = data.get('joining_date')
    )

    db.session.add(new_employee)
    db.session.commit()
    return employee_schema.jsonify(new_employee), 201


# ── READ ALL ─────────────────────────────────────────────
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return employees_schema.jsonify(employees), 200


# ── READ ONE ─────────────────────────────────────────────
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id, description=f'Employee {id} not found')
    return employee_schema.jsonify(employee), 200


# ── UPDATE ───────────────────────────────────────────────
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id, description=f'Employee {id} not found')
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    employee.first_name   = data.get('first_name',   employee.first_name)
    employee.last_name    = data.get('last_name',    employee.last_name)
    employee.email        = data.get('email',        employee.email)
    employee.phone        = data.get('phone',        employee.phone)
    employee.department   = data.get('department',   employee.department)
    employee.designation  = data.get('designation',  employee.designation)
    employee.salary       = data.get('salary',       employee.salary)
    employee.joining_date = data.get('joining_date', employee.joining_date)

    db.session.commit()
    return employee_schema.jsonify(employee), 200


# ── DELETE ───────────────────────────────────────────────
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id, description=f'Employee {id} not found')
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': f'Employee {id} deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)