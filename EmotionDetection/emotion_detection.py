from flask import Flask,request
import requests
import json
app = Flask(__name__)



def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code == 200:
        return response.json()['emotionPredictions'][0]['emotion']
    else:
        return f"Error: {response.status_code}, {response.text}"

@app.route('/get_emotion')
def get_emotion():
    text_to_analyze =  request.args.get('text')
    return emotion_detector(text_to_analyze)

if __name__ == '__main__':
    app.run(debug=True)
