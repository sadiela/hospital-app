from flask_pymongo import PyMongo
import pymongo
import flask

mongodb_client = pymongo.MongoClient("mongodb+srv://sadiela:xs5MaYfQUs8M9E5O@cluster0.ipuos.mongodb.net/healthDB?retryWrites=true&w=majority")

'''
app = flask.Flask(__name__)


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
    '''