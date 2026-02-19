"""
Emotion Detection Flask Application.

This module provides a web interface for the Emotion Detection
application using Flask.
"""
import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

# pylint: disable=wrong-import-position
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(
    "Emotion Detector",
    template_folder=os.path.join(
        os.path.dirname(__file__), '..', 'templates'
    ),
    static_folder=os.path.join(
        os.path.dirname(__file__), '..', 'static'
    )
)


@app.route("/emotionDetector")
def emotion_detection():
    """
    Detect emotions in the given text.

    Retrieves text from query parameters, analyzes it using the
    emotion_detector function, and returns formatted results.
    Returns an error message for invalid or blank input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the index page of the application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
