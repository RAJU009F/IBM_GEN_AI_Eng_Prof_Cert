from flask import Flask, render_template
from EmotionDetection import emotion_detection

app =  Flask('Emotion Detection App')

@app.route("/emotionDetector/<string:input_stmt>")
def emotionDetector(input_stmt):
    #input_stmt = "I love my life"
    response =  emotion_detection.emotion_detector(input_stmt)
    output = """For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. 
     The dominant emotion is <b>{}.""".format(response['anger'], response['disgust'],response['fear'],response['joy'],response['sadness'],response['dominant_emotion'],)
    
    return output
    #return render_template('index.html', res=response)

if __name__ == '__main__':
    app.run(port=5000,debug=True)

