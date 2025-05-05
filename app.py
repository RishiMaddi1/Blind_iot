from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "ESP32-CAM Flask Server is running"

@app.route('/upload', methods=['POST'])
def upload_image():
    if request.data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        with open(filepath, 'wb') as f:
            f.write(request.data)
        
        print(f"[+] Image saved: {filepath}")
        return jsonify({"status": "success", "filename": filename}), 200
    else:
        return jsonify({"status": "no data received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
