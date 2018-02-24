from flask import Flask
from config import mongo
from user.views import user

app = Flask(__name__)
mongo.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.register_blueprint(user)
    app.run(host='0.0.0.0', port=9009, debug=True)
