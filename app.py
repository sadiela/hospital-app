from flask import Flask, Blueprint
#from flask_restful import Api, Resource, url_for
from chat_module.chat import chat_blueprint
from device_module.device import device_blueprint
from database_module.mongo_database import mongodb_client

app = Flask(__name__)
#app.config['MONGO_URI'] = "mongodb+srv://sadiela:xs5MaYfQUs8M9E5O@cluster0.ipuos.mongodb.net/healthDB?retryWrites=true&w=majority"

app.register_blueprint(chat_blueprint, url_prefix='/chat')
app.register_blueprint(device_blueprint, url_prefix='/device')

if __name__ == '__main__':
    app.run(debug = True)