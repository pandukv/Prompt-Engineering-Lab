import os
from openai import OpenAI

# Initialize the client using the Groq API base URL and environment variable
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

# Execute the naïve prompt as defined in the experimental procedure
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user", 
            "content": "Write a one-paragraph bio of Ada Lovelace."
        }
    ]
)

# Print the output for lab observation
print("--- Naïve Prompt Output ---")
print(response.choices[0].message.content)
#print(response.output_text)
