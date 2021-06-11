from app import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    company = db.Column(db.Enum('Nestle', 'Roshen', 'Svitoch'), nullable=False)
    date_shipped = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', '{self.price}', '{self.amount}', '{self.amount}', " \
               f"'{self.date_shipped}', '{self.company}'')\n"


db.create_all()


