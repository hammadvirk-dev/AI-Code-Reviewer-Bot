# AI-Code-Reviewer-Bot 🤖
### Your Personal Senior Developer in a Box
AI-Code-Reviewer-Bot is a high-performance CLI tool designed to bridge the gap between writing code and shipping production-grade software. Powered by Google's **Gemini 2.5 Flash**, it performs deep static analysis to catch what linters miss.
## 🌟 Why Use This?
 * **For Junior Developers:** Get instant feedback on your PRs. Learn *why* a certain pattern is bad and how to fix it before your lead sees it.
 * **For Senior Developers:** Automate the "boring" parts of code review. Focus on high-level architecture while the bot catches syntax quirks, security flaws, and logic errors.
 * **For DevOps Engineers:** Ensure scripts are secure and optimized for performance before deployment.
## 📊 Sample Report Preview
When you run the bot, you receive a structured markdown report:
> **🔍 POTENTIAL BUGS**
>  * Line 42: The list_users function fails if the database returns None.
> **🛡️ SECURITY VULNERABILITIES**
>  * High: Hardcoded API key found in config.py.
>  * Medium: Input not sanitized in the search query.
> **🚀 REFACTORED CODE**
> ```python
> # Optimized version with proper error handling and env vars
> import os
> api_key = os.getenv("API_KEY")
> ...
> 
> ```
> 
## 🚀 Installation & Usage
### 1. Clone the Repo
```bash
git clone [https://github.com/hammadvirk-dev/AI-Code-Reviewer-Bot.git](https://github.com/hammadvirk-dev/AI-Code-Reviewer-Bot.git)
cd AI-Code-Reviewer-Bot

```
### 2. Install Dependencies
```bash
pip install -r requirements.txt

```
### 3. Run the Reviewer
```bash
python code_reviewer.py path/to/your/code.py

```
## 🛠️ Built With
 * **Python**: Core logic and CLI interaction.
 * **Gemini API**: Advanced LLM for deep code understanding.
 * **DevOps Principles**: Clean code, modularity, and error handling.
## 👨‍💻 Contact & Developer
**Developer:** Hammad Virk
**Profile:** github.com/hammadvirk-dev
**Portfolio:** Full Repository List
## 🏷️ Tags
#CodeReview #Python #AI #DevOps #OpenSource #ProgrammingTools #CleanCode #GeminiAPI #SoftwareEngineering #Automation #StaticAnalysis #GitHubViral
