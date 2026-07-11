from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Final Project: Emotion Detection")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    return f"For the given statement, the system response is \
    'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, \
    'joy': {response['joy']} and 'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(port=5000)