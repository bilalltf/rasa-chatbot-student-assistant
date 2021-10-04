from flask import Flask, jsonify
from flask_cors import CORS
import speech_recognition as sr
app = Flask(__name__)
CORS(app)
r = sr.Recognizer()
    
@app.route("/voice")
def voice():
    with sr.Microphone() as source: 
        audio = r.listen(source, timeout=10, phrase_time_limit=60)
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.8
        try:
            message = r.recognize_google(audio, language="fr-FR")  
        except:
            message = ""
    return jsonify(result=message)


if __name__ == '__main__':
    app.run()

