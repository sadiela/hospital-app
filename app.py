from flask import Flask
#from flask_restful import Api, Resource, url_for
from chat_module.chat import chat_blueprint
from device_module.device import device_blueprint
from admin_module.admin import admin_blueprint
#from database_module.mongo_database import mongodb_client

app = Flask(__name__)

app.register_blueprint(chat_blueprint, url_prefix='/chat')
app.register_blueprint(device_blueprint, url_prefix='/device')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug = True)