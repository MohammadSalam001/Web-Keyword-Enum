import requests
from bs4 import BeautifulSoup
import re

def extract_keywords(url):
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print(f"❌ Failed to fetch {url}. Status Code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract meta keywords
        keywords = []
        meta_keywords = soup.find("meta", attrs={"name": "keywords"})
        if meta_keywords and "content" in meta_keywords.attrs:
            keywords.extend(meta_keywords["content"].split(","))

        # Extract meta description
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description and "content" in meta_description.attrs:
            keywords.extend(meta_description["content"].split())

        # Extract all visible text
        for script in soup(["script", "style"]):  # Remove scripts and styles
            script.extract()
        text = soup.get_text()
        
        # Find words using regex (filtering out symbols and numbers)
        words = re.findall(r'\b[A-Za-z]{3,}\b', text)  # Words with at least 3 letters
        keywords.extend(words)

        # Remove duplicates and sort
        keywords = sorted(set([word.strip().lower() for word in keywords]))

        return keywords

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return []

def save_wordlist(keywords, filename="keywords_wordlist.txt"):
    with open(filename, "w") as f:
        for word in keywords:
            f.write(word + "\n")
    print(f"✅ Wordlist saved as '{filename}' ({len(keywords)} words)")

if __name__ == "__main__":
    target_url = input("🔍 Enter the target website URL: ").strip()
    extracted_keywords = extract_keywords(target_url)

    if extracted_keywords:
        save_wordlist(extracted_keywords)
    else:
        print("❌ No keywords found.")
