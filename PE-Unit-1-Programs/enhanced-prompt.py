import os
from openai import OpenAI

# Initialize the client using the Groq API base URL and environment variable
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

# The enhanced prompt string combines the three required structural elements
enhanced_prompt = (
    "You are an expert historian. [Role Framing] "
    "Provide a detailed bio of Ada Lovelace, focusing on her work with "
    "Charles Babbage and the Analytical Engine. [Specificity] "
    "Write this in exactly one academic paragraph. [Format Instructions]"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": enhanced_prompt}
    ]
)

print("--- Enhanced Output ---")
print(response.choices[0].message.content)

