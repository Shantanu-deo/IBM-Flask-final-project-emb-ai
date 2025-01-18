import json
import requests
def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text
        }
    }
    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code == 200:
        return response.json()['emotionPredictions'][0]['emotion']
    elif response.status_code == 400:
        invalidEmotionDict=  { "anger": None,"disgust": None,
        "fear": None,"joy": None,"sadness": None}
        return invalidEmotionDict
    else:
        return f"Error: {response.status_code}, {response.text}"


