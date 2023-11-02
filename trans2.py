import json
import requests
import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav
sound = AudioSegment.from_mp3("/home/aryan-khandelwal/hackathon/test1.wav")
sound.export("transcript.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

        print("Transcription: " + r.recognize_google(audio))
filez = r.recognize_google(audio)



##summarization part start
api_key = "d595447e-4865-41de-b2f1-021378818b5b"
url = "https://api.oneai.com/api/v0/pipeline"



headers = {
    "api-key": api_key,
    "content-type": "application/json"
}
payload = {
    "input": filez,
    "input_type": "article",
    "output_type": "json",
    "multilingual": {
        "enabled": True
    },
    "steps": [
        {
            "skill": "summarize"
        },
        {
            "skill": "keywords"
        }
    ],
}

r = requests.post(url, json=payload, headers=headers)
data = r.json()
print(data)

##json_file = json.loads(data)

if 'utterance' in data:
    utternace_text = data['utterance']
    print(utterance_text)

##summarization part end

