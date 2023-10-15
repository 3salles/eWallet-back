from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from hmac import compare_digest
from auth.blacklist import BLACKLIST

properties = reqparse.RequestParser()
properties.add_argument('name', type=str)
properties.add_argument('username', type=str, required=True, help="The field 'username' can not be left empty")
properties.add_argument('password', type=str, required=True, help="The field 'password' can not be left empty")

class User(Resource):
    def get(self, uid):
        user = UserModel.find_user(uid)

        if user:
            return user.to_json()
        return {'message': 'User not found'}, 404
    
    @jwt_required()
    def delete(self, uid):
        user = UserModel.find_user(uid)

        if user:
            try:
                user.delete_user()
            except:
                return {'message: ', 'An internal error ocurred trying to delete user.'}, 500
            return {'message': 'User deleted'}
        
        return {'message': 'User not found.'}, 404

class UserRegister(Resource):
    def post(self):
        data = properties.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "The username '{}' already exists.".format(data['username'])}, 409
        
        user = UserModel(**data)
        user.save_user()
        return {'message': 'User created successfully'}, 201

class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = properties.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user and compare_digest(user.password, data['password']):
            access_token = create_access_token(identity=user.uid)
            return {'access_token': access_token}, 200
        return {'message': 'The username or password is incorrect'}, 401
    
class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {"message": "Logged out successfuly!"}, 200