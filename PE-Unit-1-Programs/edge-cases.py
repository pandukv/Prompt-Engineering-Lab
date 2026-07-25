import os
from openai import OpenAI

# Setup: Ensure your API key is configured as done in Lab 1
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"
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

print("--- Lab 4: Diagnosing Prompt Failures & Edge Cases ---\n")

# Step 1: Craft a vague prompt 
vague_prompt = "Give me some good things to eat."
print("Step 1: Vague Prompt")
print(f"Prompt: {vague_prompt}")
print(f"Output (Failure Mode: Ambiguity/Missing Context):\n{get_response(vague_prompt)}")
print("-" * 40)

# Step 2: Refine the prompt by adding examples and clarifying instructions
refined_prompt = """
I am looking for a high-protein, vegetarian dinner recipe that takes less than 30 minutes to make. 
Please provide the response in the exact following format:
Recipe Name:
Prep Time:
Ingredients List:
Instructions:

Example:
Recipe Name: Quick Tofu Stir-Fry
Prep Time: 15 minutes
Ingredients List: Tofu, broccoli, soy sauce, garlic...
Instructions: 1. Press tofu... 2. Chop vegetables... 3. Stir-fry...
"""
print("Step 2: Refined Prompt")
print(f"Prompt: {refined_prompt}")
print(f"Output (Fixed with clarification and examples):\n{get_response(refined_prompt)}")
print("\n")