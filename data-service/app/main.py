from flask import Flask, request, jsonify
# from flask_cors import CORS

app = Flask(__name__)

# CORS(app)

MESSAGE_FILE = 'messages.txt'


@app.route('/messages', methods=['POST'])
def save_message():
    """Save a message to the file."""
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({"error": "Message is required"}), 400

    with open(MESSAGE_FILE, 'a') as f:
        f.write(message + '\n')
    return jsonify({"message": "Message saved successfully"}), 200


@app.route('/messages', methods=['GET'])
def get_messages():
    """Retrieve all saved messages."""
    try:
        with open(MESSAGE_FILE, 'r') as f:
            messages = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        messages = []

    return jsonify(messages), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
