import sqlite3

from flask import Flask, request, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse

import inputValidator as inputValidator

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@auth.get_password
def get_password(username):
    if username == 'root':
        return 'toor'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


class BookAPI(Resource):

    def get(self):

        query_parameters = request.args

        id = query_parameters.get('id')
        published = query_parameters.get('published')
        author = query_parameters.get('author')

        query = "SELECT * FROM books WHERE"

        to_filter = []

        if id:
            query += ' id=? AND'
            to_filter.append(id)
        if published:
            query += ' published=? AND'
            to_filter.append(published)
        if author:
            query += ' author=? AND'
            to_filter.append(author)

        # if not (id or published or author):
        #     return page_not_found(404)

        query = query[:-4] + ';'
        conn = sqlite3.connect('books.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        results = cur.execute(query, to_filter).fetchall()
        return results, 404


class BookListAPI(Resource):
    def get(self):
        conn = sqlite3.connect('books.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_books = cur.execute('SELECT * FROM books;').fetchall()
        return all_books


class LoginAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('ip', required=True, help="Error: No IP address provided. Please specify an IP!")
        super(LoginAPI, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        if 'ip' in args:
            if inputValidator.is_valid_ipv4_address(args['ip']):
                return "Assigned IP: " + args['ip']
            else:
                return "Invalid IP address"
        else:
            return "Error: No IP address provided. Please specify an IP."


class VMConfigAPI(Resource):

    def get(self):
        args = request.args
        results = {}
        if 'vmName' in args:
            results.update({'vmName': args['vmName']})
        if 'adptNumber' in args:
            results.update({'adptNumber': args['adptNumber']})
        if 'src_ip' in args:
            src_ip = args['src_ip']
            if inputValidator.is_valid_ipv4_address(src_ip):
                results.update({'src_ip': src_ip})
            else:
                results.update({'src_ip': "Invalid Input"})
        if 'dst_ip' in args:
            dst_ip = args['dst_ip']
            if inputValidator.is_valid_ipv4_address(dst_ip):
                results.update({'dst_ip': dst_ip})
            else:
                results.update({'dst_ip': "Invalid Input"})
        if 'srcPrt' in args:
            results.update({'srcPrt': args['srcPrt']})
        if 'dstPrt' in args:
            results.update({'dstPrt': args['dstPrt']})
        if bool(args):
            return results
        return "Invalid Request, No Inputs Provided"

class VMStatusAPI(Resource):

    def get(self):
        args = request.args
        if 'mgrstatus' in args:
            return "Status: Fine!"
        else:
            return "Invalid Request, No Inputs Provided"

    def post(self):
        args = request.args
        if 'vmName' in args:
            if not args['vmName']:
                return "Invalid Request, Empty Field Provided"
            else:
                return {'vmName': "Capture the Flag"}
        return "Invalid Request, No Inputs Provided"

class VMStartAPI(Resource):

    def get(self):
        args = request.args
        if 'vmName' in args:
            if not args['vmName']:
                return "Invalid Request, Empty Field Provided"
            else:
                return {'vmName': "Capture the Flag"}
        return "Invalid Request, No Inputs Provided"

class VMSuspendAPI(Resource):

    def get(self):
        args = request.args
        if 'vmName' in args:
            if not args['vmName']:
                return "Invalid Request, Empty Field Provided"
            else:
                return {'vmName': "Capture the Flag"}
        return "Invalid Request, No Inputs Provided"

api.add_resource(BookAPI, '/api/v2/resources/books')
api.add_resource(VMConfigAPI, '/api/v2/resources/vm/manage/config')
api.add_resource(VMStatusAPI, '/api/v2/resources/vm/manage/status')
api.add_resource(VMStatusAPI, '/api/v2/resources/vm/manage/start')
api.add_resource(VMStatusAPI, '/api/v2/resources/vm/manage/suspend')
api.add_resource(BookListAPI, '/api/v2/resources/books/all')
api.add_resource(LoginAPI, '/api/v2/resources/login')

if __name__ == '__main__':
    app.run()
