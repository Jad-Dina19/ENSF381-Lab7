import re 
import requests 
from bs4 import BeautifulSoup 
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
headers = { 
    "User-Agent": "lab07-web-analyzer" 
} 
try: 
    response = requests.get(url, headers=headers) 
    response.raise_for_status()  # Ensures the request was successful 
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(f"Successfully fetched content from {url}")
    tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "a", "p"])
    print(f"Tag counts: {len(tags)}")

    # print the count of each tag type
    tag_counts = {}
    for tag in tags:
        tag_name = tag.name
        if tag_name in tag_counts:
            tag_counts[tag_name] += 1
        else:
            tag_counts[tag_name] = 1
    print("Tag type counts:")
    for tag_name, count in tag_counts.items():
        print(f"{tag_name}: {count}")

except Exception as e: 
    print(f"Error fetching content: {e}") 
    
# print(soup.prettify()) 

lowercase_text = soup.get_text().lower()
words = re.findall(r'\b\w+\b', lowercase_text) 

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
    
print ("\nTop 5 most common words:")
top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
for word, freq in top_words:
    print(f"{word}: {freq}")

