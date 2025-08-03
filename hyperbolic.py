import requests
import time
import random
import signal
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HYPERBOLIC_API_KEY")

if not API_KEY:
    print("Error: NOUS_API_KEY environment variable not set.")
    sys.exit(1)

URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def generate_random_question():
    topics = [
        "technology", "science", "history", "health", "space", "AI", "finance", "travel", "sports", "food",
        "education", "psychology", "philosophy", "nature", "entertainment", "medicine", "biology", "physics",
        "economics", "politics", "literature", "engineering", "artificial intelligence", "climate change", "geography",
        "mathematics", "robotics", "social media", "cybersecurity", "ethics", "mental health", "astronomy", "quantum mechanics"
    ]
    actions = [
        "explain", "describe", "tell me about", "how does", "what is", "why is", "what are the benefits of",
        "what are the challenges of", "what are the latest developments in", "how can we improve", "how does it impact society",
        "what are the risks of", "how does it compare to", "what are some interesting facts about"
    ]
    
    specifics = [
        "in modern society", "in the next decade", "for beginners", "for experts", "in simple terms", "in detail", "with examples",
        "from a historical perspective", "from a scientific perspective", "in the context of business", "in education", "in healthcare"
    ]
    
    topic = random.choice(topics)
    action = random.choice(actions)
    specific = random.choice(specifics)
    return f"{action} {topic} {specific}?"

def send_chat_request(question):
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

def signal_handler(sig, frame):
    print("\nProgram dihentikan oleh pengguna. Keluar...")
    sys.exit(0)

def run_chat_bot():
    print("Starting automated chat bot...")
    question_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        question = generate_random_question()
        question_count += 1
        
        print(f"\nQuestion {question_count}: {question}")
        answer = send_chat_request(question)
        print(f"Answer: {answer}")
        
        delay = random.uniform(60, 120)
        print(f"Waiting {delay:.1f} seconds before next question...")
        time.sleep(delay)

if __name__ == "__main__":
    run_chat_bot()