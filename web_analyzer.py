import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
headers = {
"User-Agent": "lab07-web-analyzer"
}

def data_analysis(soup):
    rs1 = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    
    print("Headers: ",len(rs1))

    rs2 = soup.find_all("a")

    print("Links: ", len(rs2))

    rs3 = soup.find_all("p")
    print("Paragraphs: ", len(rs3))

    display([len(rs1), len(rs2), len(rs3)])

def word_frequency_analysis(soup):
    text = soup.get_text()
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    print("\nTop 5 words:")
    top_words = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:5]

    for key, value in top_words:
        print(f"{key}, {value}")

def key_word_search(soup):
    user_text = input("enter text you would like to search for\n").lower().strip() 
    text = soup.get_text().lower()
    words = re.findall(r'\b' + re.escape(user_text) + r'\b', text)
   

    print("Count: ", len(words))

def find_longest_paragraph(soup):
    rs = soup.find_all('p')
    longest = ""
    max = 0
    for element in rs:
        text = element.get_text().strip()
        if(len(text) > max):
            max = len(text)
            longest = text

    print("Longest paragraph:")
    print(longest)
    print("Length:", len(longest.split()))

def display(counts):
    labels = ["Headings", "Links", "Paragraphs"]

    plt.bar(labels, counts)
    plt.title('Put your Group 31 Here')
    plt.ylabel('Count')
    plt.savefig('web_analysis_results.png') # Save the figure as an image file
    plt.show()


    
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    data_analysis(soup)
    word_frequency_analysis(soup)
    key_word_search(soup)
    find_longest_paragraph(soup)

except Exception as e:
    print(f"Error fetching content: {e}")



