from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


def request_checker():
    parser = reqparse.RequestParser()
    parser.add_argument("X-Test-Header1", location='headers', required=False)
    parser.add_argument("X-Test-Header2", location='headers', required=False)
    parser.add_argument("test")
    args = parser.parse_args()

    response = 'OK'

    if args['test'] is not None:
        response = response + str(args['test'])

    if args['X-Test-Header1'] is not None:
        if args['X-Test-Header1'] == "one":
            response = response + 'h1'
        else:
            return "Header 1 wrong", 400

    if args['X-Test-Header2'] is not None:
        if args['X-Test-Header2'] == "two":
            response = response + 'h2'
        else:
            return "Header 2 wrong", 400

    return response, 200


class Test(Resource):

    def get(self):
        return request_checker()

    def post(self):
        return request_checker()

    def put(self):
        return request_checker()

    def delete(self):
        return request_checker()


api.add_resource(Test, "/")


if __name__ == '__main__':
    app.run(debug=True)
