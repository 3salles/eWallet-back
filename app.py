from flask import Flask
from flask_restful import  Api
from resources.transaction import Transactions, Transaction

app = Flask(__name__)
api = Api(app)


api.add_resource(Transactions, '/transactions')
api.add_resource(Transaction, '/transactions/<string:uid>')

if __name__ == '__main__':
    app.run(debug=True)