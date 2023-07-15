from flask_restful import Resource, reqparse
from models.transaction import TransactionModel

transactions = [
    {'category': 'entertainment',
    'date': '2023-06-17',
    'amount': 300,
    'description': 'Hogwarts Legacy',
    'institution': 'PS Store',
   'uid': '752d013d-4a7d-48c7-993c-87f8296757c8'},
   {
    'category': 'food',
    'date': '2023-06-17',
    'amount': 300,
    'description': 'Sanduíche',
    'institution': 'Swbway',
    'uid': '008b2d8f-7bc3-4241-b156-1122574635e5',
  },
  {
    'category': 'shopping',
    'date': '2023-06-17',
    'amount': 300,
    'description': 'Capa para celular',
    'institution': 'Shopping',
    'uid': 'e5b01419-e3ea-4998-9016-5bec1464a909',
  },
  {
    'category': 'income',
    'date': '2023-06-17',
    'amount': 4567.23,
    'description': 'Salário',
    'institution': None,
    'uid': '33f0d30f-d117-40e7-ac04-46b56165abd6',
  },
  {
    'category': 'transportation',
    'date': '2023-06-17',
    'amount': 26.12,
    'description': 'Uber',
    'institution': 'Uber',
    'uid': '908e8857-9d3e-4da8-a2e2-c6eb38948b0c',
  },
  {
    'category': 'housing',
    'date': '2023-06-17',
    'amount': 354.95,
    'description': 'Conta de luz',
    'institution': 'Equatorial',
    'uid': 'fdc055aa-2c8b-4ea1-a4c1-5e0e88a39f6c',
  },
]

class Transactions(Resource):
    def get(self):
        return {'transactions': transactions}
    

class Transaction(Resource):
    properties = reqparse.RequestParser()
    properties.add_argument('category')
    properties.add_argument('date')
    properties.add_argument('amount')
    properties.add_argument('description')
    properties.add_argument('institution')

    def find_transaction(uid):
        for transaction in transactions:
            if transaction['uid'] == uid:
                return transaction
        return None

    def get(self, uid):
        transaction = Transaction.find_transaction(uid)

        if transaction:
            return transaction
        return {'message': 'Transaction not found'}, 404

    def post(self, uid):
        data = Transaction.properties.parse_args()
        
        transaction_object = TransactionModel(uid, **data)
        new_transaction = transaction_object.to_json()

        transactions.append(new_transaction)
        return new_transaction, 200

    def put(self, uid):
        data = Transaction.properties.parse_args()
        transaction_object = TransactionModel(uid, **data)
        new_transaction = transaction_object.to_json()
        transaction = Transaction.find_transaction(uid)

        if transaction:
            transaction.update(new_transaction)
            return new_transaction, 200

        transactions.append(new_transaction)
        return new_transaction, 201

    def delete(self, uid):
        global transactions
        transactions = [transaction for transaction in transactions if transaction['uid'] != uid]
        return {'message': 'Transaction deleted'}