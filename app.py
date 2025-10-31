import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    data = {
        "method": request.method,
        "headers": dict(request.headers),
        "body": request.get_json(silent=True),
        "args": request.args.to_dict(),
        "path": request.path
    }
    print(json.dumps(data))
    return "OK", 200


@app.route('/poc', methods=['GET', 'POST', 'PUT', 'DELETE'])
def poc():
    data = {
        "info": "Subdomain takeover PoC by 13ph03nix",
        "method": request.method,
        "headers": dict(request.headers),
        "body": request.get_json(silent=True),
        "args": request.args.to_dict(),
        "path": request.path
    }
    print(json.dumps(data))
    if '13ph03nix' not in request.args:
        return "OK", 200
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(error):
    data = {
        "method": request.method,
        "headers": dict(request.headers),
        "body": request.get_json(silent=True),
        "args": request.args.to_dict(),
        "path": request.path
    }
    print(json.dumps(data))
    return "OK", 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000)
