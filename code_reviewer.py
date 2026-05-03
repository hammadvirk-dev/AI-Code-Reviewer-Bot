```python
import os
import sys
import time
import google.generativeai as genai
from typing import Optional

# Configuration
# The environment provides the API key at runtime as an empty string per instructions
API_KEY = "" 

def setup_gemini():
    """Initializes the Gemini API with exponential backoff logic."""
    if not API_KEY:
        # In a real local environment, the user would set this.
        # For this tool, we assume the environment injects it.
        pass
    
    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

def get_ai_response(model, prompt: str):
    """Fetches AI completion with exponential backoff (up to 5 retries)."""
    retries = 5
    for i in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            if i == retries - 1:
                return "Error: Failed to reach AI services after multiple attempts. Please check your connection or API key."
            time.sleep(2**i) # 1s, 2s, 4s, 8s, 16s

def conduct_review(file_path: str):
    """Reads the file and sends it to Gemini for a structured review."""
    if not os.path.exists(file_path):
        print(f"[-] Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        return

    print(f"[*] Analyzing '{file_path}' with AI...")
    
    model = setup_gemini()
    
    system_prompt = """
    You are a Senior DevOps Engineer and Full-Stack Developer. 
    Perform a deep "Code Review" on the following code.
    Structure your response as follows:
    1. 🔍 POTENTIAL BUGS: Identify logic flaws or crashes.
    2. 🛡️ SECURITY VULNERABILITIES: Spot SQLi, XSS, hardcoded keys, etc.
    3. 🚀 PERFORMANCE & LOGIC: Identify bottlenecks.
    4. ✨ REFACTORED CODE: Provide a complete, optimized version of the code.
    5. 💡 LEARNING TIPS: Briefly explain 'why' for the changes.
    """
    
    user_prompt = f"Review this code:\n\n```{file_path.split('.')[-1]}\n{code_content}\n```"
    
    full_prompt = f"{system_prompt}\n\n{user_prompt}"
    
    review_report = get_ai_response(model, full_prompt)
    
    print("\n" + "="*50)
    print("AI CODE REVIEW REPORT")
    print("="*50)
    print(review_report)
    print("="*50)

if __name__ == "__main__":
    print("🤖 AI-Code-Reviewer-Bot | Created by Hammad Virk")
    if len(sys.argv) < 2:
        target_file = input("Enter the path to the code file you want to review: ")
    else:
        target_file = sys.argv[1]
    
    conduct_review(target_file)

```
          
