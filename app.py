from flask_restful import  Api
from resources.transaction import Transactions, Transaction
from flask_openapi3 import OpenAPI, Info, Tag
from extensions.database import database
import extensions.cors as cors
from schemas.transaction import TransactionSchema, ListTransactionsSchema, AddTransactionSchema, DeleteTransactionSchema
from schemas.error import ErrorSchema
from logger import logger


# http://127.0.0.1:5000/openapi/swagger#

def create_app():
    info = Info(title="eWallet API", version="0.1.0")
    app = OpenAPI(__name__, info=info)
    
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ewallet.db'
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

    api.add_resource(Transactions, '/transactions')
    api.add_resource(Transaction, '/transactions/<string:uid>')

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
    import extensions.database as database
    
    database.init(app)
    app.run(debug=True)