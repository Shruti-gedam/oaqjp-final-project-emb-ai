"""Flask server for the Emotion Detector web application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def root():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze the text provided by the web page."""
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze or not text_to_analyze.strip():
        return "Please enter text to analyze."
    result = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
