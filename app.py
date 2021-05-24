from flask import Flask, jsonify, request

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
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    #iterate over stores
    for store in stores:
        if store['name'] == name:
            #if the store name matches, return i
            return jsonify(store)
    
    #if none match, return an error message
    return jsonify({'message': f'store {name} not found'})

# GET /store
@app.route('/store')
def get_stores():
    #jsonify returns a JSON dictionary, cannot return directly the stores array as its in Python
    #JSON always uses double quotes ", never single quotes ' to enclose keys and strings.
    return jsonify({'stores':stores}) 

# POST /STORE/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    #iterate over stores
    for store in stores:
        if store['name'] == name:
            #if the store name matches, add the item
            request_data = request.get_json()
            new_store_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_store_item)
            return jsonify({'item': new_store_item})
    
    #if none match, return an error message
    return jsonify({'message': f'store {name} not found'})
    

# GET /STORE/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    #iterate over stores
    for store in stores:
        if store['name'] == name:
            #if the store name matches, return the dictionary with an arrany of items
            return jsonify({'items':store['items']})
    
    #if none match, return an error message
    return jsonify({'message': f'store {name} not found'})

app.run(host='0.0.0.0', port=4000, debug=True)
