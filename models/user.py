from extensions.database import database
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserModel(database.Model):
    __tablename__ = 'users'

    uid = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = database.Column(database.String(100))
    nickname = database.Column(database.String(100))
    password = database.Column(database.String(100))

    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password
    
    def to_json(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'nickname': self.nickname,
        }
    
    @classmethod
    def find_user(cls, uid):
        user = cls.query.filter_by(uid=uid).first()
        
        if user:
            return user
        return None 
    
    @classmethod
    def find_by_nickname(cls, nickname):
        user = cls.query.filter_by(nickname=nickname).first()
        
        if user:
            return user
        return None 
    
    def save_user(self):
        database.session.add(self)
        database.session.commit()


    def delete_user(self):
        database.session.delete(self)
        database.session.commit()