from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self):
        return todos

    def post(self):
        temp = request.json
        for key in temp:
            todos[key] = temp[key]
        return todos

api.add_resource(TodoSimple, '/')

if __name__ == '__main__':
    app.run(debug=True)