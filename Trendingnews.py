from GoogleNews import GoogleNews
googlenews= GoogleNews()
googlenews= GoogleNews(period="7d")
topic = input("Enter the news you want to know about")
googlenews.search(topic)
result = googlenews.result()
print(topic+" News")
for x in result:
 print("-"*50)
 print("Title--", x['title'])
 print("Description--", x['desc'])