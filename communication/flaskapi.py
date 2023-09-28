import logging
from flask import Flask

# create Flask object
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/')
def hello_world():
    app.logger.debug("Hehehe")
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)