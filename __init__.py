from flask import Flask, jsonify, request, render_template

import rest_handler

# creating a Flask app

app = Flask(__name__, template_folder='templates')


@app.route('/v1/api/resource/<resource_type>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def endpoint(resource_type):
    if request.method == 'POST':
        resource = rest_handler.add_resource(resource_type, request.json)
        return jsonify(resource)
    else:
        return "Not implemented yet.", 400


@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

