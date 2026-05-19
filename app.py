from flask import Flask, jsonify, request

app = Flask(__name__)

items = {}
counter = 1

@app.route('/items', methods=['POST'])
def create_item():
    global counter
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    item = {'id': counter, 'name': data['name'], 'description': data.get('description', '')}
    items[counter] = item
    counter += 1
    return jsonify(item), 201

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values())), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    data = request.get_json()
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = items.pop(item_id, None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify({'message': 'Items deleted successfully'}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
