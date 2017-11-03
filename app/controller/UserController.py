#from app.models.User import User
from app.models.model.Model import User
from app.models import db

class UserController:
    global users

    def __init__(self):
        print('ini self')
        self.users = []
    
    def register(self,username,email,password):
        if not db.session.query(User).filter(User.email==email).count():
            u = User(username, email, password)
            db.session.add(u)
            db.session.commit()
            return u.serialize()
        return None

    def login(self, email, password):
        for user in User.query.filter(User.email == email):
            if(user.email == email and user.password== password):
                return True;
        return False;

    def register_memory(self, username, email, password):
        f = False;
        if(len(self.users)==0):
            user = User(username, email, password)
            self.users.append(user.serialize())
            return self.users

        for user in self.users:
            if(user['username']== username and user['password']==password):
                    f = True;
        if(f!=True):
            user = User(username, email, password)
            self.users.append(user.serialize())
        return self.users

    def login_memory(self, email, password):
        for user in self.users:
            if(user['email']==email and user['password']==password):
                return True

        return False;
    
