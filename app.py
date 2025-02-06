from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Dockerized Flask!"

@app.route("/api/voice-to-text", methods=["POST"])
def voice_to_text():
    audio = request.files["file"]
    return jsonify({"message": "语音已接收", "filename": audio.filename})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

