def readnews(topic,page,count):
 googlenews.get_page(page)
 result = googlenews.page_at(page) 
 print(topic+" News")
 for x in result:
  print("-"*50)
  print("Title--", x['title'])
  # print("Image--", x['img'])
  print("Description--", x['desc'])
  count = count+10
 valcondition = input("Do you want to know more:(Answer in Y Or N) ")
 if valcondition == 'Y':
  readnews(topic,page+1,count) 
 elif valcondition == 'N':
  valtopiccondition = input("Do You want to change the topic:(Answer in Y or N) ")
  if valtopiccondition == "Y":
    topic = input("Enter the news you want to know about ")
    page = 1
    googlenews.search(topic)
    # result = googlenews.result()
    readnews(topic,page,count)
 
from GoogleNews import GoogleNews
googlenews= GoogleNews()
googlenews= GoogleNews(period="7d")
topic = input("Enter the news you want to know about")
googlenews.search(topic)
# result = googlenews.result()
page = 1
count = 0
readnews(topic,page,count)
# print("The total amount news that we have read is "+str(count))