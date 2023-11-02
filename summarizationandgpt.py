import requests
##summarization part start
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
##summarization part end

##GPT part start
api_key = "0G8JXZAH09BZ1BEVYB09BIJLYB8W2Y4TPDZDI4HI9LNUM9EE9UJ95P0VEZ5RBHDY"
endpoint = "https://jamsapi.hackclub.dev/openai/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

messages = []

chat_over = False

while not chat_over:
    user_question = input("Enter a question or type 'quit' to end the chat: ")
    if user_question.lower() == "quit":
        chat_over = True
        break
    messages.append({"role": "user", "content": user_question})
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        assistant_answer = result["choices"][0]["message"]["content"]
        print(assistant_answer)
        messages.append({"role": "assistant", "content": assistant_answer})
    else:
        print(f"Request failed: {response.reason}")
        chat_over=True

##GPT part end