from flask import Flask, jsonify
from flask_restx import Resource, Api

from src.Conversor import Conversor


# instantiate the app
app = Flask(__name__)

api = Api(app)


class API_Version(Resource):
    def get(self):
        return jsonify({
            'status': 'success',
            'result': 'v2'
        })

class API_Conversor(Resource):
    def get(self, f):
        ''' Convierte de ºF a ºC '''
        #c = (f - 32) * 5 / 9 
        conv = Conversor()
        c = conv.fahrenheit_to_centigrados(f)
        return jsonify({
            'status': 'success',
            'input' : f,
            'result': round(c, 2)
        })

api.add_resource(API_Version, '/myapi/version')
api.add_resource(API_Conversor, '/myapi/f2c/<int:f>')
api.add_resource(API_Conversor, '/myapi/f2c/<float:f>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)