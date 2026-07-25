import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def get_llm_response(prompt):
    """
    Executes the prompt using the Groq API with the Llama3-8b model.
    """
    print(f"--- Sending Prompt ---\n{prompt}\n")
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0, # Low temperature for consistent classification
        max_tokens=80, # Short response needed for sentiment labels
    )
    
    return completion.choices[0].message.content.strip()

# The input text we want to classify 
test_input = "The interface was a bit clunky, but the overall performance was surprisingly fast."

# 1. Zero-Shot Prompt 
# Provides instructions without any examples.
zero_shot_prompt = f"""
Classify the sentiment of the following text as Positive, Negative, or Neutral.

Text: {test_input}
Sentiment:
"""

# 2. Few-Shot Prompt 
# Provides 3 exemplar input-output pairs to guide the model.
few_shot_prompt = f"""
Classify the sentiment of the text. Use the following examples as a guide:

Input: The battery life is incredible and lasts all day.
Output: Positive

Input: I found the setup process to be extremely confusing and frustrating.
Output: Negative

Input: The package arrived on time, but the box was slightly dented.
Output: Neutral

Input: {test_input}
Output:
"""

def run_lab_experiment():
    print("Executing Zero-Shot Performance Benchmark...")
    zero_shot_result = get_llm_response(zero_shot_prompt)
    print(f"Zero-Shot Result: {zero_shot_result}\n")

    print("Executing Few-Shot Performance Benchmark...")
    few_shot_result = get_llm_response(few_shot_prompt)
    print(f"Few-Shot Result: {few_shot_result}\n")

    # Lab Instructor Analysis
    print("--- Lab Analysis ---")
    print("Note how the Few-Shot prompt provides 'exemplars' to guide the model's tone and output format [2, 3].")
    print("Compare if the Zero-Shot response is as concise as the Few-Shot response.")

if __name__ == "__main__":
    run_lab_experiment()
