class TransactionModel:
    def __init__(self, uid, category, date, amount, description, institution):
        self.uid = uid
        self.category = category
        self.date = date
        self.amount = amount
        self.description = description
        self.institution = institution

    def to_json(self):
        return {
            'uid': self.uid,
            'category': self.category,
            'date': self.date,
            'amount': self.amount,
            'description': self.description,
            'institution': self.institution
        }