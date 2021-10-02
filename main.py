import json
import os
import sqlite3
import time
from seleniumrequests import Chrome
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import requests
import database
import downloadpost
import getindex
import getinfo

# 首頁
import getstroies
import init


print("Enter account: ")
account = input()
print("Enter password:　")
password = input()
# account
# password


url_main = 'https://www.instagram.com/'
browser = webdriver.Chrome()
browser.get(url_main)

# 等待100s 以讀取網頁
browser.implicitly_wait(100)
# 登入
islogin = True

elem_user = browser.find_element_by_name("username").send_keys(account)
elem_password = browser.find_element_by_name("password").send_keys(password)
elem_submit = browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
time.sleep(10)

database_name = 'Instagram.db'
# 取得資料/目標網址
username = '''mamamoo_official'''
url_main = init.url_main
url_Target = init.url_main + username + '/'

# 取得資料Post
# result = getinfo.main(browser, url_Target, islogin, database_name, username)
# user_id=267920419
# cursor='QVFBeGtwREpmNEgzZnVrOHB4LTlVa0xmM2NEbW1paGdaT3c5SEE2XzV1TVJxOFl2ckFmcXFiTDl2dGxZODVxVlZybG5mNHdESWx5bmFsb2F1OGpEMlFJQg=='
# uri_page2 = init.uri_query.format(user_id=user_id, cursor=cursor)
# result = getinfo.main_continue(browser, uri_page2, islogin,cursor, user_id, database_name,username)
# print("DB all over")

# 下載Post
# downloadpost.main(islogin, browser, database_name, username)

# 限時動態
# getstroies.main(browser, username, islogin)

# 更新POST LIST
# getinfo.refresh(browser, url_Target, islogin, database_name, username)


# 輪詢更新 get user info + 限時
browser.implicitly_wait(5)
users_list = database.getTablename(database_name)
for i in users_list:
    print(i[0]+"...", end='')
    user_name = i[0]
    url_main = init.url_main
    url_Target = init.url_main + user_name + '/'
    # getindex.main(islogin, browser, url_Target)
    try:
        getindex.main(islogin, browser, url_Target)
        time.sleep(1)
        try:
            print(user_name +"get stories...",end="")
            getstroies.main(browser, user_name, islogin)
            print("OVER!!")
        except:
            print("FAIL!!")

    except:
        print(i[0] + "is fail")




# 輪詢更新POST LIST
# users_list = database.getTablename(database_name)
# for i in users_list:
#     print(i[0] + "...", end='')
#     user_name = i[0]
#     url_main = init.url_main
#     url_Target = init.url_main + user_name + '/'
#     try:
#         getinfo.refresh(browser, url_Target, islogin, database_name, user_name)
#         print("refresh OK!!:" )
#     except:
#         print("refresh FAIL!! :")
