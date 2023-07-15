from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Transactions(Resource):
    def get(self):
        return {'transactions': 'my transactions'}
    
api.add_resource(Transactions, '/transactions')

if __name__ == '__main__':
    app.run(debug=True)