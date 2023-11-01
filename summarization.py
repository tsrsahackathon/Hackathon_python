import requests

api_key = "d595447e-4865-41de-b2f1-021378818b5b"
url = "https://api.oneai.com/api/v0/pipeline"

with open("<FILE PATH>", "rb") as f:
    text = f.read()

headers = {
    "api-key": api_key,
    "content-type": "application/json"
}
payload = {
    "input": text,
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
