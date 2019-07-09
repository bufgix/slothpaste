import requests
from bs4 import BeautifulSoup

payload = {
    'poster': 'test',
    'syntax': 'text',
    'content': 'hey',
}

req = requests.post("https://paste.ubuntu.com", data=payload)
req2 = requests.get('https://paste.ubuntu.com')
soup = BeautifulSoup(req2.text, 'html.parser')

with open("langs.txt", "w") as f:
    for select in soup.find_all('option'):
        if select.get('value'):
            l = select.get('value')
            print(l)
            f.write(f"{l}\n")