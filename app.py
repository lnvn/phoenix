from flask import Flask, redirect, request, render_template
from pymongo.mongo_client import MongoClient
import os

# uri = "mongodb://root:root@localhost/"
uri = "mongodb://root:root@localhost:27017/"
# uri = os.environ.get('MONGO_URI')
client = MongoClient(uri)

# client = MongoClient('db',
#                      username='root',
#                      password='root',
#                      )

# ----- Check DB connection and authentication
# try:
#     client.admin.command('ping')
#     print("Ping db success!")
# except Exception as e:
#     print(str(e))

DATABASE_NAME = 'message'
COLLECTION_NAME = 'my_message'
db = client[DATABASE_NAME]
db_collection = db[COLLECTION_NAME]

app = Flask(__name__)

@app.route('/')
def index():
    messages = db_collection.find().sort('_id', 1)
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    content = request.form['message']
    if content:
        db_collection.insert_one({'content': content})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')