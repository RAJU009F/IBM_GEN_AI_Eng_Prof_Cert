''' 
Flask application of Emotion detecttion
App will run @ localhost:5050.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector ")

@app.route("/")
def render_index():
    ''' This function initiates the rendering home page
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from request and
        runs emotion_detector function. 
        The output returned shows dominant emotion along with other 5 emotions with scores
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if not response['dominant_emotion']:
        return "<b>Invalid text! Please try again!.</b>"


    formatted_response = "For the given statement, the system response is " + \
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " + \
    f"'fear': {response['fear']}, " + \
    f"'joy': {response['joy']} and 'sadness': {response['sadness']}." + \
    f" The dominant emotion is <b>{response['dominant_emotion']}</b>."

    return formatted_response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
