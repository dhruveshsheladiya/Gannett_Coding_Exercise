# all require modules for REST API
from flask import Flask, request #FLask is most light weight framework for Python API and Web Development based on Jinja2 template Engine
from flask_restful import Resource, Api
from sqlalchemy import create_engine #SQLAlchemy is an open source SQL toolkit and object-relational mapper for the Python programming language released under the MIT License.
from json import dumps #JSON is javaScript Object Notion that uses Human-readable text to transmit data Objects
from flask import jsonify

#Database Connection
db_connect = create_engine('sqlite:///produce.db')
#Application Initialization
app = Flask(__name__)
api = Api(app)

#Below class designed for serving Welcome message for Product Inventory database
class APIWelcome(Resource):
    def get(self):
        return {'Welcome to Product Inventory API': 'You can view productInventory Table, product_code and product_Name'}

'''Below class designed to serving all data of produceInventory Database
It will return JSON object of All Products of produceInventory Database
It will Return "No such Table found" Exception if Table Name is given Incorrectly
'''
class produceInventory(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        try:
            query = conn.execute("select * from produceInventory") # Performs query and returns json result
        except:
            return jsonify({"error": "No Such Table Found"}), 400 #Returns Error message
        data = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return {'produceInventory': data}  # Fetches the Data from the Table


'''Below class designed to serving specific data based on produce_code {id }
It will return JSON object of Array of corresponding produce_code from the Table
It will Return "No such record found" Exception if produce_code is not present in the Table.
'''

class produce_code(Resource):
    def get(self, code):
        conn = db_connect.connect()
        if len(code)!=19:
            return jsonify({"error": "Invalid Operation or Input"})
        try:
            query = conn.execute("select * from produceInventory where produce_code = ?",(code,))
        except:
            return jsonify({"error": "No Such record found"}), 400

        data=[dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        if data==None:
            return jsonify({"error": "No Such record found"}), 400
        #result = {'Inventory has': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        else:
            result = {'Inventory has': data}
        return jsonify(result)
		
'''Below class designed to serving specific data based on produce_name {name: Lattes, Peach}
It will return JSON object of Array of corresponding produce_name from the Table
It will Return "No such record found" Exception if produce_name is not present in the Table.
'''
class produce_name(Resource):
    def get(self, item_name):
        conn = db_connect.connect()
        if len(item_name) == 0:
            abort(404)

        try:
            query = conn.execute("select * from produceInventory where produce_name = ?",(item_name,))

            '''
            By using I can say that My API is robust enough to handle and boycott the SQL Injection Attacks to the WebApplication
            Parameterized Query always prevents the malicious attack to the API via Inputs
            '''
        except:
            return jsonify({"error": "No Such record found"}), 400
        result = {'Inventory found records of this iteam': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


'''Below class designed to serving specific data based on produce_unitprice {UnitPrice}
It will return JSON object of Array of corresponding produce_unitprice from the Table
It will Return "No such record found" Exception if produce_unitprice is not present in the Table.
'''
class produce_unitprice(Resource):
    def get(self, unitprice):
        conn = db_connect.connect()
        if len(name) == 0:
            abort(404)
        try:
            query = conn.execute("select * from produceInventory where produce_unitprice =%d "  %int(unitprice))
        except:
            return jsonify({"error": "No Such record found"}), 400
        result = {'We have these iteams of Unite Price': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(APIWelcome, '/') # Route 0; Gives homepage view
api.add_resource(produceInventory, '/produceInventory') # Route_1; Gives Table view
api.add_resource(produce_code, '/produceInventory/<code>', endpoint='produce_code') # Route_2 ; Gives corresponding produce_code Row view
api.add_resource(produce_name, '/produceInventory/<item_name>', endpoint='produce_name') # Route_3 Gives corresponding produce_name view
api.add_resource(produce_unitprice, '/produceInventory/<unitprice>', endpoint='produce_unitprice') # Route_4 Corresponding produce_unitprice view


#Initialize the Main
if __name__ == '__main__':
     app.run(port='8000')
