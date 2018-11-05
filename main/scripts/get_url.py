#!/usr/bin/env python

import os
import bs4
import urllib
import datetime
from bs4 import BeautifulSoup

CSS_SELECTOR_ITEM = ".js-item-slider"

url = "https://www.avito.ru/sankt-peterburg/fototehnika/zerkalnye_fotoapparaty?s_trg=3&q=canon+60D"
d = datetime.datetime.today()
listLinkOld = []
listLinkNew = []
listDiff = []

pageFileName = "./files/html_"+d.strftime("%Y%m%d%H%M%S")+".txt"
linksOldFileName = "./files/links_old.txt"
linksNewFileName = "./files/links_new.txt"
#linksDiffFileName = "./files/links_diff.txt"

urllib.urlretrieve(url, pageFileName)
fileHtml = open(pageFileName, "r")
soup = BeautifulSoup(fileHtml,features="html.parser")

if os.access(linksOldFileName, os.F_OK) == True:
    print("File exists")
else:
    linksOldFile = open(linksOldFileName, "w")    
    linksOldFile.close()

linksNewFile = open(linksNewFileName, "w")
#getting links from page code
for a in soup.select(CSS_SELECTOR_ITEM):
    link = a.get("href") 
    linksNewFile.write(link + "\n")

linksNewFile.close()
#reading file to list
try:
    with open(linksOldFileName, "r") as linksFile:
        for line in linksFile:
            #deleting the last empty line in the file
            currentPlace = line[:-1]
            #adding line to the end of the list
            listLinkOld.append(currentPlace)
except IOError:
    print("An IOError has occurred. It looks as file is not exists.")

with open(linksNewFileName, "r") as linksFile:
    for line in linksFile:
        #deleting the last empty line in the file
        currentPlace = line[:-1]
        #adding line to the end of the list
        listLinkNew.append(currentPlace)

#list for sending
listDiff = list(set(listLinkNew)-set(listLinkOld))

os.unlink(linksOldFileName)

os.rename(linksNewFileName, linksOldFileName)

print(listDiff)

#print soup.find_all("div", ".item")    
#print soup.select(".js-item-slider")
#soup = soup.select(".js-item-slider")
#print soup.find_all("a")

#print soup.select(".item.item_table.clearfix.js-catalog-item-enum.js-item-extended.item_table_extended.snippet-experiment.item_hide-elements")

#file = open("./files/html.txt", "w")
#file.write(html)
#file.close()
#def get_url_to_file()  h