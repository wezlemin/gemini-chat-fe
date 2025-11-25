import requests

# Add your Gemini API key here.
API_KEY = 'AIzaSyBs3y7_t9CWaZ1sLX05t9_E6grsNYv1ITg'
MODEL = 'gemini-pro'
API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={API_KEY}'

def send_to_gemini(user_message, system_instruction=None):
    headers = {'Content-Type': 'application/json'}
    parts = [{"text": user_message}]
    body = {"contents": {"parts": parts}}
    # If you want a system instruction, add like this:
    if system_instruction:
        body["systemInstruction"] = {"parts": [{"text": system_instruction}]}
    response = requests.post(API_URL, headers=headers, json=body)
    if response.status_code == 200:
        resp_data = response.json()
        candidates = resp_data.get("candidates", [])
        if candidates and candidates[0].get("content", {}).get("parts"):
            return candidates[0]["content"]["parts"][0]["text"]
        else:
            return "No response received from Gemini."
    else:
        return f"Gemini API Error: {response.status_code} - {response.text}"

def main_chat():
    print("Welcome to Gemini Chatbot. Type 'quit' to exit.")
    while True:
        user_in = input("You: ")
        if user_in.lower() == 'quit':
            break
        bot_out = send_to_gemini(user_in, system_instruction="You are a friendly AI assistant.")
        print(f"Gemini: {bot_out}")

if __name__ == "__main__":
    main_chat()
