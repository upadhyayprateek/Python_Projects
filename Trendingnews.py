def readnews(topic,page):
 googlenews.get_page(page)
 result = googlenews.page_at(page) 
 print(topic+" News")
 for x in result:
  print("-"*50)
  print("Title--", x['title'])
  # print("Image--", x['img'])
  print("Description--", x['desc'])
 valcondition = input("Do you want to know more:(Answer in Y Or N) ")
 if valcondition == 'Y':
  readnews(topic,page+1) 
 elif valcondition == 'N':
  valtopiccondition = input("Do You want to change the topic:(Answer in Y or N) ")
  if valtopiccondition == "Y":
    topic = input("Enter the news you want to know about ")
    page = 1
    googlenews.search(topic)
    # result = googlenews.result()
    readnews(topic,page)
 
from GoogleNews import GoogleNews
googlenews= GoogleNews()
googlenews= GoogleNews(period="7d")
topic = input("Enter the news you want to know about")
googlenews.search(topic)
# result = googlenews.result()
page = 1
readnews(topic,page)


