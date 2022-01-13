from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json, sys, os

app = Flask(__name__)
api = Api(app)
port = 4242

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("You said port is : {} ".format(port))


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    with open('tmp/data.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
    return jsonify(records)

@app.route('/api/v1/resources/book', methods=['GET'])
def query_records():
    id = request.args.get('id')
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            print(type(record['id']), int(id))
            if record['id'] == int(id):
                return jsonify(record)
        return jsonify({'error': 'data not found'})

@app.route('/api/v1/resources/book', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        json.dump(records, f)
    return jsonify(records)

@app.route('/api/v1/resources/book/d', methods=['DELETE'])
def delete_record():
    record = int(request.args.get('id'))
    new_records = []
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['id'] == record:
                continue
            new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(new_records)


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=port)