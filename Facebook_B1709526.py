from selenium import webdriver #selenium ket noi 
from time import sleep
from selenium.webdriver.common.keys import Keys
import json

#chromedriver de truy cap gg
browser = webdriver.Chrome(executable_path="./chromedriver") 
browser.get("https://www.facebook.com/")
#Tai khoan facebook.com
txtUser = browser.find_element_by_id("email") 
#user test
txtUser.send_keys("cuongnguyenkyky@gmail.com") 
# Mat khau facebook.com
txtPass =  browser.find_element_by_id("pass")
#pass test
txtPass.send_keys("Phaihoila1") 
 #Login
txtPass.send_keys(Keys.ENTER)
#Cho sever phan hoi
sleep(5)
#Link bai viet bat ky muon crawl du lieu 
browser.get("https://www.facebook.com/PhimHayMoiNgay216/posts/2774444176170365?__tn__=-R0.g") 
#Crawl comment 

comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
#print (comment_list)
class Insert (object):
      def __init__(self, poster, comment):
        self.poster = poster
        self.comment = comment
   
list=[]
for comment in comment_list:
    #hien thi ten nguoi vao comment
    poster = comment.find_element_by_class_name("_6qw4")
    content = comment.find_element_by_class_name("_3l3x")
    print ("*",poster.text,".",content.text)
    insert = Insert(poster.text,content.text)
    list.append(insert.__dict__)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(list, file)
    #file.download('data.json')

sleep(10)
browser.close()