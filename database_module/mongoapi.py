from flask_pymongo import PyMongo
import flask

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/health_db")
db = mongodb_client.db

@app.route("/add_one", methods=['POST'])
def add_chat():
    result = db.chat.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message=str(result.acknowledged))

@app.route("/", methods=['GET'])
def home():
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])

@app.route("/get_sessionchats/<int:sessionid>", methods=["GET"])
def get_sessionchats(sessionId):
    sessionChats = db.chat.find({'sessionid': sessionId})
    return flask.jsonify([chat for chat in sessionChats])

if __name__ == '__main__':
    app.run(debug = True)