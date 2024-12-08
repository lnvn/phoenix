from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config

# Initialize Flask app and database
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Create the Image model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Initialize the database
@app.before_request
def create_tables():
    db.create_all()

# Check if the file type is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Index Route (optional)
@app.route('/')
def index():
    return "Welcome to the Image Sharing Website"

# Upload Route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file to disk
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(filepath)

        # Save the image info to the database
        new_image = Image(filename=filename)
        db.session.add(new_image)
        db.session.commit()

        return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
    return jsonify({"error": "File not allowed"}), 400

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route to list all uploaded images
@app.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    images_list = [{"id": img.id, "filename": img.filename, "uploaded_at": img.uploaded_at} for img in images]
    return jsonify(images_list)

if __name__ == '__main__':
    app.run(debug=True)
