from GoogleNews import GoogleNews
googlenews= GoogleNews()
googlenews= GoogleNews(period="7d")
googlenews.search('India')
result= googlenews.result()
for x in result:
 print("-"*50)
 print("Title--", x['title'])
 print("Description--", x['desc'])