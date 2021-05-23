from flask import Flask

app = Flask(__name__)

stores = [
    {
    'name': 'My Wonderful Store',
    'items': [
        {
        'name': 'My Item',
        'price': 15.99
        }
    ]
    }
]


# POST - used to receive data
# GET  - used to send data back only
#app.route(...) declares the endpoints and link with a python function


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    pass

# POST /STORE/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /STORE/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(host='0.0.0.0', port=4000, debug=True)
