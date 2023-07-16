from extensions.database import database
from utils.date_utils import convert_to_python_time
from datetime import datetime

class TransactionModel(database.Model):
    __tablename__ = 'transactions'

    uid = database.Column(database.String, primary_key=True)
    category = database.Column(database.String(50))
    date = database.Column(database.DateTime, default=datetime.today)
    amount = database.Column(database.Float(precision=2))
    description = database.Column(database.String(140))
    institution = database.Column(database.String(140))

    def __init__(self, uid, category, date, amount, description, institution):
        self.uid = uid
        self.category = category
        self.date = convert_to_python_time(date)
        self.amount = amount
        self.description = description
        self.institution = institution
    
    def to_json(self):
        return {
            'uid': self.uid,
            'category': self.category,
            'date': self.date.isoformat(),
            'amount': self.amount,
            'description': self.description,
            'institution': self.institution
        }
    
    @classmethod
    def find_transaction(cls, uid):
        transaction = cls.query.filter_by(uid=uid).first()
        
        if transaction:
            return transaction
        return None 
    
    def save_transaction(self):
        database.session.add(self)
        database.session.commit()

    def update_transaction(self, category, date, amount, description, institution):
        if date is not None:
            self.date = convert_to_python_time(date)
        else:
            self.date = datetime.now()
        
        self.category = category
        self.amount = amount
        self.description = description
        self.institution = institution

    def delete_transaction(self):
        database.session.delete(self)
        database.session.commit()