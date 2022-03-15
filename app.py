from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from chat_module.chat_api import chat_blueprint
from device_module.device import device_blueprint

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the api home"

app.register_blueprint(chat_blueprint, url_prefix='/chat')
app.register_blueprint(device_blueprint, url_prefix='/device')

if __name__ == '__main__':
  
    app.run(debug = True)