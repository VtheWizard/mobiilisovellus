from flask_restful import Resource
from auth import Auth

class User(Resource):
    def get(self, id):
        if id == "me":
            return {"message": "Hello me"}
        else:
            return {"message": id}

class Login(Resource):
    def get(self):
        return {"message": "login_success",
        "apikey": Auth.createApiKey(1)}


class Register(Resource):
    def put(self):
        return {"message": "register_success"}
