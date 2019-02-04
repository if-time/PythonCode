from flask import Flask

from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def hello_world():
    client = MongoClient('localhost', 27017)
    db = client.pythondb
    posts = db.posts
    return posts.find_one()


if __name__ == '__main__':
    app.run()
