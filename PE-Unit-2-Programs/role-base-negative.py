import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def get_llm_response(prompt):
    """
    Simulates a call to an LLM. 
    Replace this with actual API calls to observe real model influence.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0, # Low temperature for consistent classification
        max_tokens=80, # Short response needed for sentiment labels
    )
    
    return completion.choices[0].message.content.strip()
    print(f"--- Sending Prompt ---\n{prompt}\n")
    # For demonstration, we return a mock response that follows the constraints
    return "To begin investing in technology, consider broad-market index funds or sector-specific ETFs rather than individual companies."

# 1. Role-Based Prompt
# Establishing the persona (e.g., "You are a financial advisor...")
role_based_persona = "You are a financial advisor providing advice to a beginner investor."
user_query = "What are the best ways to start investing in the tech sector?"

persona_prompt = f"""
{role_based_persona}

Question: {user_query}
Answer:
"""

# 2. Negative Prompting
# Adding a constraint to suppress undesired content (e.g., "Do not mention brand names") 
negative_constraint = "Do not mention any specific brand names or company names in your response."

combined_prompt = f"""
{role_based_persona}
{negative_constraint}

Question: {user_query}
Answer:
"""

def run_persona_lab():
    print("Step 1: Evaluating Role-Based Prompt influence...")
    response_1 = get_llm_response(persona_prompt)
    print(f"Persona-Only Response: {response_1}\n")

    print("Step 2: Evaluating influence of Negative Prompting...")
    response_2 = get_llm_response(combined_prompt)
    print(f"Persona + Negative Constraint Response: {response_2}\n")

    # Evaluation instructions for the lab session
    print("--- Lab Instructor Analysis ---")
    print("1. Influence: How did the financial advisor persona change the tone compared to a generic model?")
    print("2. Suppression: Did the second response successfully avoid mentioning specific brands (e.g., Apple, Microsoft) as instructed?")
    print("3. Trade-offs: Did the negative constraint make the advice too vague, or was it still helpful?")

if __name__ == "__main__":
    run_persona_lab()