from flask_restful import  Api
from resources.transaction import Transactions, Transaction
from resources.user import User, UserRegister, UserLogin, UserLogout
from flask_openapi3 import OpenAPI, Info, Tag
from extensions.database import database
import extensions.cors as cors
from schemas.transaction import TransactionSchema, ListTransactionsSchema, AddTransactionSchema
from schemas.error import ErrorSchema
from logger import logger
from flask_jwt_extended import JWTManager
from auth.blacklist import BLACKLIST
from flask import jsonify


def create_app():
    info = Info(title="eWallet API", version="0.1.0")
    app = OpenAPI(__name__, info=info)
    
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ewallet.db'
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'eWallet'
    app.config['JWT_BLACKLIST_ENABLED'] = True

    jwt = JWTManager(app)
    

    @jwt.token_in_blocklist_loader
    def is_in_blacklist(self, token):
        return token['jti'] in BLACKLIST
    
    @jwt.revoked_token_loader
    def access_token_invalid():
        return jsonify({'message': 'You have been logged out.'}), 401

    api.add_resource(Transactions, '/transactions')
    api.add_resource(Transaction, '/transactions/<string:uid>')
    api.add_resource(User, '/users/<string:uid>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogout, '/logout')

    

    cors.init(app)
    database.init_app(app)


    return app

app = create_app()

produto_tag = Tag(name="Transactions", description="Add, create, edit and delete a transaction")

@app.get('/transactions', tags=[produto_tag], responses={'200': ListTransactionsSchema})
def get_transactions():
    logger.debug('Fetching transactions')

@app.post('/transactions/{uid}', tags=[produto_tag], responses={'200': AddTransactionSchema, "409": ErrorSchema, "400": ErrorSchema} )
def add_transaction(form: TransactionSchema):
    transaction = Transaction(**form)
    logger.debug(f"Transaction '{transaction.name}' created")
    
@app.get('/transactions/{uid}', tags=[produto_tag], responses={'200': TransactionSchema, '404': ErrorSchema})
def get_transaction(uid: str):
    logger.debug(f"Searching for #{uid} transaction.")

@app.put('/transactions/{uid}',  tags=[produto_tag], responses={'200': AddTransactionSchema, '201': AddTransactionSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_transaction(form: TransactionSchema):
    transaction = Transaction(**form)
    logger.debug(f"Transaction '{transaction.name}' edited")

@app.delete('/transactions/{uid}', tags=[produto_tag], responses={'200': TransactionSchema, '404': ErrorSchema, '400': ErrorSchema})
def delete_transaction(uid:str):
    logger.debug(f"Transaction #'{uid}' deleted")

if __name__ == '__main__':
    
    app.run( host='0.0.0.0', port=5001)