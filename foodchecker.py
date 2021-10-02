from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser= webdriver.Chrome()
#create the variable for webdriver
# browser = webdriver.Chrome(executable_path='/path/to/geckodriver')
# driver = webdriver.Chrome(r"C:\Users\USER_NAME\Desktop\FOLDER\chromedriver")
browser = webdriver.Chrome(executable_path='path/to/folder/chromedriver')
#it will open the browser and search for the URL below

browser.get('https://www.caloriemama.ai/api')

#find the class name
upload = browser.find_element_by_class_name('file-upload')

#enter you image file location and here send image
upload.send_keys("/path/to/food.jpeg")
time.sleep(5)

#return tje value by the class name
get  = browser.find_element_by_class_name('group-name')
print(get.text)