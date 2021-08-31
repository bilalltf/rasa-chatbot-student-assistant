import os
from flask import Flask, render_template, redirect, url_for,request, jsonify
from flask import make_response
from flask_cors import CORS
import speech_recognition as sr
app = Flask(__name__)
CORS(app)

@app.route('/voice')
def voiceTotext():
    r = sr.Recognizer()  
    with sr.Microphone() as source: 
        print("Speak Anything :")
        audio = r.listen(source) 
        try:
            message = r.recognize_google(audio, language="fr-FR")  

        except:
            message = "Erreur"

    while len(message)==0:
        continue
    return jsonify(result=message)


if __name__ == '__main__':
    app.run()

