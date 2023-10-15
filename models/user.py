from extensions.database import database
import uuid

class UserModel(database.Model):
    __tablename__ = 'users'

    uid = database.Column(database.String(), primary_key=True)
    name = database.Column(database.String(100))
    username = database.Column(database.String(100))
    password = database.Column(database.String(100))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.uid = str(uuid.uuid4())
    
    def to_json(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'username': self.username,
        }
    
    @classmethod
    def find_user(cls, uid):
        user = cls.query.filter_by(uid=uid).first()
        
        if user:
            return user
        return None 
    
    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        
        if user:
            return user
        return None 
    
    def save_user(self):
        self.uid = str(uuid.UUID(self.uid))
        database.session.add(self)
        database.session.commit()

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()