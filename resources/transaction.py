from flask_restful import Resource, reqparse
from models.transaction import TransactionModel
from flask_jwt_extended import jwt_required

class Transactions(Resource):
    @jwt_required()
    def get(self):
        return {'transactions': [transaction.to_json() for transaction in TransactionModel.query.all()]}

class Transaction(Resource):
    properties = reqparse.RequestParser()
    properties.add_argument('category')
    properties.add_argument('date')
    properties.add_argument('amount')
    properties.add_argument('description')
    properties.add_argument('institution')

    @jwt_required()
    def get(self, uid):
        transaction = TransactionModel.find_transaction(uid)

        if transaction:
            return transaction.to_json()
        return {'message': 'Transaction not found'}, 404
    
    @jwt_required()
    def post(self, uid):
        if TransactionModel.find_transaction(uid):
            return {'message': "Transaction id already exists."}, 400
        
        data = Transaction.properties.parse_args()
        new_transaction = TransactionModel(uid, **data)
        
        try:
            new_transaction.save_transaction()
        except:
            return {'message': 'An internal error ocurred trying to save transaction.'}, 500
        return new_transaction.to_json()
    
    @jwt_required()
    def put(self, uid):
        data = Transaction.properties.parse_args()
        transaction_found = TransactionModel.find_transaction(uid)

        if transaction_found:
            transaction_found.update_transaction(**data)
            transaction_found.save_transaction()
            return transaction_found.to_json(), 200
        
        new_transaction = TransactionModel(uid, **data)
        
        try:
            new_transaction.save_transaction()
        except:
            return {'message: ', 'An internal error ocurred trying to edit transaction.'}, 500
        return new_transaction.to_json(), 201

    @jwt_required()
    def delete(self, uid):
        transaction = TransactionModel.find_transaction(uid)

        if transaction:
            try:
                transaction.delete_transaction()
            except:
                return {'message: ', 'An internal error ocurred trying to delete transaction.'}, 500
            return {'message': 'Transaction deleted'}
        
        return {'message': 'Transaction not found.'}, 404

