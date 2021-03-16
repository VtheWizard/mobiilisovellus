from flask import Flask
from flask_restful import Api, Resource
from user import User, Login, Register

app = Flask(__name__)
api = Api(app)

api.add_resource(User, "/user/<id>")
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
