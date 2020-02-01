from main import db
from models.sales import  Sales


class Inventories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    sales = db.relationship('Sales', backref='inventory', lazy=True)

    def add_records(self):
        db.session.add(self)
        db.session.commit()

    # Fetch all reords
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    #fetch one record
    @classmethod
    def fetch_one_record(cls,id):
        return cls.query.get(id)#.first()