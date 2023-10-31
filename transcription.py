import oneai
import requests
import time
import json
from urllib.parse import urlencode

with open("C:/Users/riddh/PycharmProjects/pythonProject/test.mp3", "rb") as f:
    text = f.read()

api_key = "d595447e-4865-41de-b2f1-021378818b5b"
pipeline = {
    "include_empty_outputs": True,
    "input_type": "article",
    "multilingual": {
        "enabled": True,
        "expected_languages": ["en"]
    },
    "steps": [
        {
            "skill": "transcribe",
            "params": {
                "engine": "whisper",
                "timestamp_per_word": False,
                "language": "en",
            }
        }
    ],
    "output_type": "json",
    "multilingual": {
        "enabled": True,
        "expected_languages": ["en"]
    },
    "content_type": "audio/mp3"
}
url = "https://api.oneai.com/api/v0/pipeline/async/file?" + urlencode({"pipeline": json.dumps(pipeline)})

headers = {
    "api-key": api_key,
    "content-type": "audio/mp3"
}

r = requests.post(url, text, headers=headers)
data = r.json()

get_url = f"https://api.oneai.com/api/v0/pipeline/async/tasks/{data['task_id']}"
while (True):
    r = requests.get(get_url, headers=headers)
    response = r.json()

    if response['status'] != "RUNNING":
        break

    time.sleep(5)


var = response
print(var)

