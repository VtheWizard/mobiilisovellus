from flask_restful import Resource
from auth import Auth

class User(Resource):
    def get(self, id):
        if id == "me":
            return {"msg": "Hello me"}
        else:
            return {"msg": id}

class Login(Resource):
    def get(self):
        return {"msg": "login_success",
        "apikey": Auth.createApiKey(1)}


class Register(Resource):
    def get(self):
        return {"msg": "register"}
