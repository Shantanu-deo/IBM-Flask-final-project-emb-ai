from flask import Flask,request
import requests
import json
app = Flask(__name__)

@app.route('/get_emotion')
def emotion_detector():
    text_to_analyze =  request.args.get('text')
    print(text_to_analyze)

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
    response = requests.get(url, headers=headers, params={"data": json.dumps(input_json)})
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == '__main__':
    app.run(debug=True)
