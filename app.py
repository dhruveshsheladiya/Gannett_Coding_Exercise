from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify
from flask import jsonify
'''try:
    import flask_jsonpify.jsonify
except:
    from flask.ext.jsonpify import jsonify'''


db_connect = create_engine('sqlite:///produce.db')
app = Flask(__name__)
api = Api(app)

		
class produceInventory(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from produceInventory") # This line performs query and returns json result
        return {'produceInventory': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class produce_code(Resource):
    def get(self, code):
        conn = db_connect.connect()
        if len(code)==0:
            abort(404)
        query = conn.execute("select * from produceInventory where produce_code = ?",(code,))
        result = {'Inventory has': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
		

class produce_name(Resource):
    def get(self, iteam_name):
        conn = db_connect.connect()
        if len(name) == 0:
            abort(404)
        query = conn.execute("select * from produceInventory where produce_name = ?",(iteam_name,))
        result = {'Inventory found records of this iteam': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)



class produce_unitprice(Resource):
    def get(self, unitprice):
        conn = db_connect.connect()
        if len(name) == 0:
            abort(404)
        query = conn.execute("select * from produceInventory where produce_unitprice =%d "  %int(unitprice))
        result = {'We have these iteams of Unite Price': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(produceInventory, '/produceInventory') # Route_1

api.add_resource(produce_code, '/produceInventory/<code>', endpoint='produce_code') # Route_3
api.add_resource(produce_name, '/produceInventory/<iteam_name>', endpoint='produce_name') # Route_3

#api.add_resource(produce_code, '/produceInventory/<code>') # Route_3
api.add_resource(produce_unitprice, '/produceInventory/<unitprice>', endpoint='produce_unitprice') # Route_3

#api.add_resource(produce_name, '/produceInventory/<iteam_name>') # Route_3

if __name__ == '__main__':
     app.run(port='8000')
