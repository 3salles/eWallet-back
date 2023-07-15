from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

transactions = [
    {'category': 'entertainment',
    'date': '2023/06/17',
    'amount': 300,
    'description': 'Hogwarts Legacy',
    'institution': 'PS Store',
   'uid': '001'},
   {
    'category': 'food',
    'date': '2023/06/17',
    'amount': 300,
    'description': 'Sanduíche',
    'institution': 'Swbway',
    'uid': '002',
  },
  {
    'category': 'shopping',
    'date': '2023/06/17',
    'amount': 300,
    'description': 'Capa para celular',
    'institution': 'Shopping',
    'uid': '003',
  },
  {
    'category': 'income',
    'date': '2023/06/17',
    'amount': 4567.23,
    'description': 'Salário',
    'institution': None,
    'uid': '004',
  },
  {
    'category': 'transportation',
    'date': '2023/06/17',
    'amount': 26.12,
    'description': 'Uber',
    'institution': 'Uber',
    'uid': '005',
  },
  {
    'category': 'housing',
    'date': '2023/06/17',
    'amount': 354.95,
    'description': 'Conta de luz',
    'institution': 'Equatorial',
    'uid': '006',
  },
]

class Transactions(Resource):
    def get(self):
        return {'transactions': transactions}
    
api.add_resource(Transactions, '/transactions')

if __name__ == '__main__':
    app.run(debug=True)