"""
Emotion Detection using Watson NLP lib
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    text to be analyzed is passed to the function as an argument and is 
    stored in the variable text_to_analyze. 
    Returns: 
    The value being returned must be the text attribute of the response object
     as received from the Emotion Detection function.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    result_response = {
        'anger': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'sadness': 0,
        'dominant_emotion': ''
     }

    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code != 200:
        result_response["anger"] = None
        result_response["disgust"] = None
        result_response["fear"] = None      
        result_response["joy"] = None
        result_response["sadness"] = None
        result_response["dominant_emotion"] = None
        return result_response
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    if not emotions:
        result_response["anger"] = None
        result_response["disgust"] = None
        result_response["fear"] = None      
        result_response["joy"] = None
        result_response["sadness"] = None
        result_response["dominant_emotion"] = None
        return result_response

    result_response["anger"] = emotions.get("anger", 0)
    result_response["disgust"] = emotions.get("disgust", 0)
    result_response["fear"] = emotions.get("fear", 0)        
    result_response["joy"] = emotions.get("joy", 0)
    result_response["sadness"] = emotions.get("sadness", 0)
    result_response["dominant_emotion"] = max(emotions, key=emotions.get)

    return result_response