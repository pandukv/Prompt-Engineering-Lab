import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def get_groq_response(prompt):
    """
    Sends a prompt to the Groq API using the Llama3-8b model.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0, # Low temperature for consistent formatting
    )
    return completion.choices[0].message.content.strip()

def verify_structure(content, format_type):
    """
    A basic verification step to check if the output matches the requested structure.
    """
    if format_type == "table":
        # Check for standard Markdown table indicators: pipes and hyphens
        return "|" in content and "-|-" in content or "---" in content
    elif format_type == "list":
        # Check for common bullet point markers
        bullet_markers = ["*", "-", "•", "1."]
        return any(content.strip().startswith(marker) for marker in bullet_markers) or "\n-" in content
    return False

def run_structured_prompting_lab():
    print("--- Lab Experiment: Structured Format Prompting ---")

    # Part A: Markdown Table Prompting
    # As specified in the source: "List three benefits of daily exercise in a Markdown table..."
    table_prompt = "List three benefits of daily exercise in a Markdown table with columns 'Benefit' and 'Description.'"
    print(f"\nStep 1: Requesting Markdown Table...")
    table_output = get_groq_response(table_prompt)
    print("Response Received:")
    print(table_output)
    
    is_table_valid = verify_structure(table_output, "table")
    print(f"Verification: {'PASSED' if is_table_valid else 'FAILED'} (Markdown table structure detected)")

    # Part B: Bulleted List Prompting
    list_prompt = "List three healthy snacks in a simple bulleted list format."
    print(f"\nStep 2: Requesting Bulleted List...")
    list_output = get_groq_response(list_prompt)
    print("Response Received:")
    print(list_output)
    
    is_list_valid = verify_structure(list_output, "list")
    print(f"Verification: {'PASSED' if is_list_valid else 'FAILED'} (Bullet list structure detected)")

if __name__ == "__main__":
    run_structured_prompting_lab()