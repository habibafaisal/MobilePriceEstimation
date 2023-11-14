from facebook_page_scraper import Facebook_scraper
import json
import re

def id_generator(dict_var):
    for k, v in dict_var.items():
        if k == "content":
            yield v
        elif isinstance(v, dict):
            for id_val in id_generator(v):
                yield id_val

#instantiate the Facebook_scraper class

# page_name = "newmobilemania"


# page_name = "cellbuzz.pk"
page_name = "applewala.pk"
# page_name = "mobileriverofficial"
posts_count = 600
browser = "chrome"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 1500 #600 seconds
headless = True
meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

json_data = meta_ai.scrap_to_json()
# print(json_data)

json_data = json.loads(json_data)
# print(json_data)

print("**")
print("**")

count = 0
postsList = []
for postNumber in id_generator(json_data):
    print("Post # ", count)
    print(postNumber)
    postsList.append(postNumber)
    count = count + 1

splittedList = []

for i in range(len(postsList)):
    # x = postsList[i].split("\n")
    # x = re.split('gb|Gb|GB', postsList[i])
    # y = str.extract('[a-zA-Z]+:[0-9]+\/-', expand=False).str.strip()
    # y = re.match('[a-zA-Z]+:[0-9]+\/-', postsList[i])
    if((("gb" in postsList[i]) or ("GB" in postsList[i]) or ("Gb" in postsList[i])) and ("Iphone" in postsList[i])):
        splittedList.append(postsList[i].split("\n"))
    # splittedList.append(y)
    # print(x)
    # print('prices')
    # print(y)

# Remove Duplicates
# splittedList = list(dict.fromkeys(splittedList))


import sys
import os
import csv

print(len(splittedList))

# [a-zA-Z]+:[0-9]+\/-


columns = ['Posts']
with open('facebook_data.csv', 'a+', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # zipped_list = zip(brandsList, titlesList, conditionsList, locationsList, pricesList, finalDescription)
    writer.writerow(columns)
    #writer.writerows(zipped_list)
with open('facebook_data.csv', 'a+', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(splittedList)
    # writer.writerows(postsList)
#
# with open('posts.csv', 'a+') as csvfile:
#     for content in splittedList:
#         csvfile.write(content + '\n')