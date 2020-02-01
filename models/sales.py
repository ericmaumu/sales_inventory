from datetime import datetime
from app import db

class Sales(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    inv_id = db.Column(db.Integer, db.ForeignKey('inventories.id'))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def add_records(self):
        db.session.add(self)
        db.session.commit()

    # Fetch all reords
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    #fetch one record
    @classmethod
    def fetch_one_record(cls, id):
        return cls.query.get(id)#.first()