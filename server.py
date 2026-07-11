"""
Flask server for the Emotion Detection application.

This module provides a web interface and API endpoint for detecting
emotions in a given piece of text using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Final Project: Emotion Detection")

@app.route("/")
def index():
    """Render the main index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """
    Analyze the emotion of the text passed in the request's query parameters.

    Returns a formatted string describing the scores for each emotion
    and the dominant emotion, or an error message if the text is invalid.
    """
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
