from flask_restful import Resource
from database import mysql, query
from auth import Auth

class User(Resource):
    def get(self, id):
        result = query("SELECT * FROM users WHERE user_id = %(user_id)s",
        {"user_id": id}, True)
        return result

class Login(Resource):
    def get(self):
        return {"message": "login_success",
        "apikey": Auth.createApiKey(1)}


class Register(Resource):
    def put(self):
        return {"message": "register_success"}
