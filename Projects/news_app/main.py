import requests


query=input("What type of news are you interested in today ? ")
api="2227a813ffc34fcfa449da04bd84511e"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-03-11&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)
data=r.json()
# print(data)
articles=data["articles"]
for article in articles:
    print(f"Title : {article['title']}\n")
    print(f"Description : {article['description']}\n")
    print(f"URL : {article['url']}\n")
    print("\n******************************************\n")
   