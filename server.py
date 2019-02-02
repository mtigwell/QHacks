from flask import Flask, request
from flask_cors import CORS, cross_origin
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
CORS(app)

# API for doing search
@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('search')
    num_results = request.args.get('results')
    print(search_term, num_results)
    result = [
        {
        'url': "test.url.1",
        'summary': "this is a summary",
        'expanded': 'false'
        },
        {
        'url': "test.url.2",
        'summary': "this is a summary",
        'expanded': 'false'
        },
        {
        'url': "test.url.2",
        'summary': "this is a summary",
        'expanded': 'false'
        },
        {
        'url': "test.url.2",
        'summary': "this is a summary",
        'expanded': 'false'
        }
    ]

    return jsonify(result)

# API for expanding summary
@app.route('/expand', methods=['GET'])
def expand():
    url = request.args.get('url')
    print(url)
    result = {
        'summary': 'This is a longer summary it is so much more'
    }

    return jsonify(result)

if __name__ == '__main__':
   app.run(debug = True)