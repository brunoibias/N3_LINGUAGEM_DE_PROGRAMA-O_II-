from routes import Routes

from flask import Flask, request, json
app = Flask(__name__)

routes = Routes()


@app.route('/userCreate/', methods=['POST'])
def create_user():
    response = routes.create(request)
    return response


@app.route('/userRemove/', methods=['POST'])
def remove_user():
    response = routes.remove(request)
    return response


@app.route('/userQuery/', methods=['POST'])
def query_user():
    response = routes.query(request)
    return response


if __name__ == '__main__':
    app.run()
    use_debugger = True
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')
