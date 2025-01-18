from flask import Flask, request
from emotion_detection import emotion_detector as ED

app = Flask(__name__)

@app.route('/emotionDetector')
def get_emotion():
    """
    Endpoint to detect emotions from the provided text.

    This function retrieves the text to analyze from the query parameters,
    uses the emotion_detector function to analyze the text, and returns the
    detected emotions. If the text is invalid, it returns an error message.

    Returns:
        dict: A dictionary of detected emotions and their scores.
        str: An error message if the text is invalid.
    """
    text_to_analyze = request.args.get('text')
    all_emotions = ED(text= text_to_analyze)
    dominant_emotion_score = all_emotions.items()
    if list(dominant_emotion_score)[0][1] is None:
        return 'Invalid text! Please try again!.'
    return all_emotions

if __name__ == '__main__':
    """
    Main entry point of the application.

    Runs the Flask application in debug mode.
    """
    app.run()
