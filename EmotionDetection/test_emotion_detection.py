import unittest
from emotion_detection import emotion_detector
import importlib

import pandas as pd 
data ={'Statement' : ['I am glad this happened',
'I am really mad about this','I feel disgusted just hearing about this',
'I am so sad about this','I am really afraid that this will happen'],
'Emotion':['joy','anger','disgust','sadness','fear']}
testDF = pd.DataFrame(data) 
class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        # Example test case
        for index,rowData in testDF.iterrows():
            print (rowData)
            text_to_analyze = rowData['Statement']
            expected_output = rowData['Emotion']
            emotions_dict= emotion_detector(text_to_analyze)
            top_emotion = sorted(emotions_dict.items(), key=lambda item: item[1],reverse=True)[0][0]
            self.assertEqual(top_emotion, expected_output)

if __name__ == '__main__':
    unittest.main()
