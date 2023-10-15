from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    def get(self, uid):
        user = UserModel.find_user(uid)

        if user:
            return user.to_json()
        return {'message': 'User not found'}, 404
    
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
        properties = reqparse.RequestParser()
        properties.add_argument('name', type=str, required=True, help="The field 'name' can not be left empty")
        properties.add_argument('nickname', type=str, required=True, help="The field 'nickname' can not be left empty")
        properties.add_argument('password', type=str, required=True, help="The field 'password' can not be left empty")
        
        data = properties.parse_args()

        if UserModel.find_by_nickname(data['nickname']):
            return {"message": "The nickname '{}' already exists.".format(data['nickname'])}, 409
        
        user = UserModel(**data)
        user.save_user()
        return {'message': 'User created successfully'}, 201
