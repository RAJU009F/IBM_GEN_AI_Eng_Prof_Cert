"""
sentiment analysis using Watson NLP
"""
import json
import requests


def sentiment_analyzer(text_to_analyse):
    """
    URL: 'https://sn-watson-sentiment-bert.labs.skills.network/v1
    /watson.runtime.nlp.v1/NlpService/SentimentPredict'
    Headers: {"grpc-metadata-mm-model-id":
     "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    Input json: { "raw_document": { "text": text_to_analyse } }
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers, timeout=100)
    if response.status_code ==500:
        return {'label':None, 'score':None}

    formatted_response =  json.loads(response.text)
    score =  formatted_response['documentSentiment']['score']
    label  =  formatted_response['documentSentiment']['label']
    return {'label':label, 'score':score}
