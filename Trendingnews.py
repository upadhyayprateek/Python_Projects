def readnews(topic,page):
 googlenews.get_page(page)
 result = googlenews.page_at(page) 
 print(topic+" News")
 for x in result:
  print("-"*50)
  print("Title--", x['title'])
  # print("Image--", x['img'])
  print("Description--", x['desc'])
 val = input("Do you want to know more:(Answer in Y Or N) ")
 if val == 'Y':
  readnews(topic,page+1) 

from GoogleNews import GoogleNews
googlenews= GoogleNews()
googlenews= GoogleNews(period="7d")
topic = input("Enter the news you want to know about")
googlenews.search(topic)
result = googlenews.result()
page = 1
readnews(topic,page)