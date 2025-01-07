from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Create the app
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():

    # Get the query parameter
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return {"error": "No text provided for analysis."}, 400

    #Detect emotions with called function
    response = emotion_detector(text_to_analyze)

    #Extract values from response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    #Return in required format
    return {'message':
        'For the given statement, the system response is \'anger\': {}, \'disgust\': {}, \'fear\': {}, \'joy\': {}, \'sadness\': {}. The dominant emotion is {}.'.format(
            anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion
        )
    }

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)