import os
from mistralai import Mistral

API_KEY = ""  # just get the API key from their website https://console.mistral.ai/home which is absolutely free to get 
MODEL = "mistral-large-latest" # thier best LLM model with 65billion+ parameters

client = Mistral(api_key=API_KEY)

def ask_copilot(user_input):
    stream_response = client.chat.stream(
        model=MODEL,
        messages=[{"role": "user", "content": user_input}]
    )

    response_text = ""
    for chunk in stream_response:
        if chunk.data.choices[0].delta.content:
            text = chunk.data.choices[0].delta.content
            print(text, end="", flush=True)
            response_text += text  # Collect response
    print("\n")
    return response_text

# Continuous chat loop
print("🚀 Jarvis-like Copilot Ready! Type 'exit' to quit.\n")
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("Goodbye!")
        break
    print("Copilot: ", end="")
    ask_copilot(user_query)
