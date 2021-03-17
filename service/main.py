# core modules
from flask import Flask
from flask_restful import Api, Resource
from flask_mysqldb import MySQL
from config import api_config

# api modules
from user import User, Login, Register

# initializing app
app = Flask(__name__)
app.config['MYSQL_HOST'] = api_config['DB_HOST']
app.config['MYSQL_USER'] = api_config['DB_USER']
app.config['MYSQL_PASSWORD'] = api_config['DB_PASSWORD']
app.config['MYSQL_DB'] = api_config['DB_DB']
mysql = MySQL(app)
api = Api(app)

# test routes
class Services(Resource):
    def get(self):
        return { "message": "List of services available",
                "data": {
                    "12195015": { "service_id": "12195015", "service_provider": "Joku Oy", "service_provider_id": "2fk29942"},
                    "12195016": { "service_id": "12195016", "service_provider": "Joku Oy", "service_provider_id": "2fk29942"},
                    "12195017": { "service_id": "12195017", "service_provider": "Joku Oy", "service_provider_id": "2fk29942"},
                    "12195018": { "service_id": "12195018", "service_provider": "Joku Oy", "service_provider_id": "2fk29942"}
                }}

class Service(Resource):
    def get(self):
        pass

class Index(Resource):
    def get(self):
        return {"message": "Jobster API 0.1 beta"}


api.add_resource(Index, "/")
api.add_resource(User, "/user/<id>")
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")

api.add_resource(Services, "/services")
api.add_resource(Service, "/services/<id>")

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
