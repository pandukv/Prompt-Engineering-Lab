import os
from openai import OpenAI

# Setup: Ensure your API key is configured as done in Lab 1
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"
#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize the client using the Groq API base URL and environment variable
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

def get_response(prompt):
    """Helper function to send the prompt to the model and return the response."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # You can also use gpt-4
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print("--- Lab 3: Iterative Refinement on a Simple Task ---\n")
# Round A: Minimal instruction
prompt_a = "Summarize the plot of the Shakespearean play Romeo and Juliet."
print("Iteration A (Minimal Instruction):")
print(f"Prompt: {prompt_a}")
print(f"Output:\n{get_response(prompt_a)}")
print("-" * 40)

# Round B: Addition of length and style constraints
prompt_b = "Summarize the plot of the Shakespearean play Romeo and Juliet in exactly two sentences. Write it in the style of a dramatic movie trailer."
print("Iteration B (Length & Style Constraints):")
print(f"Prompt: {prompt_b}")
print(f"Output:\n{get_response(prompt_b)}")
print("-" * 40)

# Round C: Specification of key content elements (setting and theme)
prompt_c = """
Summarize the plot of the Shakespearean play Romeo and Juliet in exactly two sentences. 
Write it in the style of a dramatic movie trailer. 
Make sure to explicitly mention the setting of Verona and the core theme of fatal family rivalry.
"""
print("Iteration C (Setting & Theme Specified):")
print(f"Prompt: {prompt_c}")
print(f"Output:\n{get_response(prompt_c)}")
print("\n")
