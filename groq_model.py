from groq import Groq
import os

#Make sure you set your API key as an environment variable using:
#export GROQ_API_KEY="your_api_key_here"

api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY environment variable not set")

client = Groq(api_key=api_key)

def generate(prompt: str, max_tokens: int = 300, temperature: float = 0.1):
    resp = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message.content


