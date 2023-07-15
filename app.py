from flask import Flask
from flask_restful import  Api
from resources.transaction import Transactions, Transaction

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ewallet.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

@app.before_request
def create_database():
    database.create_all()

api.add_resource(Transactions, '/transactions')
api.add_resource(Transaction, '/transactions/<string:uid>')

if __name__ == '__main__':
    from database import database
    
    database.init_app(app)
    app.run(debug=True)