import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)
def get_llm_response(prompt):
    """
    Simulates a call to an LLM.
    Replace with actual API calls to observe real refinement cycles.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0, # Low temperature for consistent classification
        #max_tokens=80, # Short response needed for sentiment labels
    )
    
    return completion.choices[0].message.content.strip()
    print(f"--- Sending Prompt ---\n{prompt}")
    # Mock response for demonstration
    return "Summary output based on constraints..."

# The Technical Article (Source Task) 
technical_article = """
Quantum computing leverages the principles of quantum mechanics, such as superposition 
and entanglement, to perform calculations that are beyond the reach of classical 
supercomputers. While classical bits are either 0 or 1, qubits can exist in multiple 
states simultaneously. This allows for massive parallelism in processing complex 
algorithms, particularly in cryptography, material science, and drug discovery.
"""

# Cycle 1: Basic Prompt
# We start with an open-ended task to identify baseline failures.
basic_prompt = f"""
Summarize the following article:
{technical_article}
"""

# Cycle 2: First Refinement (Word Count Constraint)
# Adding explicit constraints based on initial length/format failures.
refined_prompt_v1 = f"""
Summarize the following article in under 15 words:
{technical_article}
"""

# Cycle 3: Second Refinement (Formatting Constraint)
# Adding further constraints like bullet points to finalize the structure.
refined_prompt_v2 = f"""
Summarize the following article in under 30 words. 
Use a bulleted list format.
{technical_article}
"""

def run_refinement_lab():
    print("Cycle 1: Issuing Basic Prompt...")
    res1 = get_llm_response(basic_prompt)
    print(f"Output 1: {res1}\n")

    print("Cycle 2: First Refinement (Length Constraint)...")
    res2 = get_llm_response(refined_prompt_v1)
    print(f"Output 2: {res2}\n")

    print("Cycle 3: Second Refinement (Bullet Format Constraint)...")
    res3 = get_llm_response(refined_prompt_v2)
    print(f"Output 3: {res3}\n")

    # Lab Documentation Step 
    print("--- Lab Instructor Analysis: Iterative Improvement ---")
    print("1. Baseline Failure: Did the basic prompt result in a summary that was too long or unformatted?")
    print("2. Constraint Adherence: Did the model stay under the 30-word limit in Cycle 2?")
    print("3. Final Refinement: How did the bullet format in Cycle 3 improve readability compared to Cycle 1?")

if __name__ == "__main__":
    run_refinement_lab()