from database import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id          = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String(50),  nullable=False)
    last_name   = db.Column(db.String(50),  nullable=False)
    email       = db.Column(db.String(120),  unique=True, nullable=False)
    phone       = db.Column(db.String(20),  nullable=True)
    department  = db.Column(db.String(100), nullable=True)
    designation = db.Column(db.String(100), nullable=True)
    salary      = db.Column(db.Numeric(12, 2), nullable=True)
    joining_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'