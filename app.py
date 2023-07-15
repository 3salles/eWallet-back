from flask import Flask
from flask_restful import  Api
from resources.transactions import Transactions

app = Flask(__name__)
api = Api(app)


api.add_resource(Transactions, '/transactions')

if __name__ == '__main__':
    app.run(debug=True)