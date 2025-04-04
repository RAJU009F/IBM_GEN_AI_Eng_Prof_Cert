import requests

'''
emotion detection function 
'''
def emotion_detector(text_to_analyze):
    '''
    takes an argument returns 
    '''
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    formatted_resp = {
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0,
            'dominant_emotion': ''
        }

    resp = requests.post(URL, json = input_json, headers=headers)
    resp_dic =  resp.json()
    
    for prediction in  resp_dic['emotionPredictions']:
        emotion_data = prediction['emotion']
        formatted_resp['anger'] = emotion_data.get('anger', 0)    
        formatted_resp['fear'] = emotion_data.get('fear', 0)
        formatted_resp['joy'] = emotion_data.get('joy', 0)
        formatted_resp['sadness'] = emotion_data.get('sadness', 0)
        formatted_resp['disgust'] = emotion_data.get('disgust', 0)

    dominant_emotion = ''
    dominant_emotion_score = 0

    for emotion in formatted_resp.keys():
        if emotion!='dominant_emotion':
            if formatted_resp[emotion] > dominant_emotion_score:
                dominant_emotion_score = formatted_resp[emotion]
                formatted_resp['dominant_emotion'] = emotion

    return formatted_resp

