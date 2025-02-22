# 🔍 Web Keyword Enum 🔍

A **cybersecurity OSINT tool** that extracts **keywords, meta tags, and visible text** from a website and saves them as a wordlist. Useful for **password cracking, social engineering, and information gathering**.

## 🚀 Features
- Extracts **meta keywords, meta descriptions, and visible text** from any website
- Filters **unique, meaningful words** (removes duplicates and unnecessary symbols)
- Saves extracted words into a **wordlist** for password cracking or OSINT research
- **Fast & lightweight** – Uses `requests` and `BeautifulSoup` for quick parsing

---

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-keyword-extractor.git
   
   cd web-keyword-extractor
  

2. Make sure you install the dependencies:
```bash
  pip install -r requirements.txt
```

## 🛠️ Usage

3. Run the script and enter the target website URL:

```bash
python web_keyword_extractor.py
```
+ Enter the target website URL: https://example.com

+ Wordlist saved as 'keywords_wordlist.txt' (150 words)
  
---

This will generates a wordlist (keywords_wordlist.txt) that can be used for brute-force attacks, dictionary-based enumeration, or OSINT research.

🔹 Example Output:
```bash
admin
contact
helpdesk
password
secure
support
username
...
```
---

## Ethical Considerations 🔒
This tool is meant for ethical hacking, OSINT research, and penetration testing. Use responsibly and do not target unauthorized websites.
