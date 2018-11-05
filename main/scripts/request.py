#!/usr/bin/env python
# coding: utf8
import ConfigParser
import requests
import json
import os
import bs4
import urllib
import datetime
from bs4 import BeautifulSoup

CSS_SELECTOR_ITEM = ".js-item-slider"

conf = ConfigParser.RawConfigParser()
conf.read(os.path.join(os.getcwd(), "../../../moskal-bot.conf"))
#print conf.get("general", "token")
token = conf.get("general", "token")
offset = 435615425

apiUrl = "https://api.telegram.org/bot"+token+"/"
activeChatsFileName = "./files/active_chats.txt"

def get_updates_json(request):
    params = {'offset': offset, 'allowed_updates': "message"}
    response = requests.get(request + 'getUpdates', data=params, verify=False)
    return response.json()

def last_updates(data):  
    results = data['result']

#    total_updates = len(results) - 1
#    print results
#    print 'new line'
#    print results[total_updates]
    return results

def get_chat_ids(updates):
    chats = {}
    for update in updates:
        #if message from user 
        if chat_type(update) == 'private':
            chat = update['message']['chat']['id']
            text = update['message']['text']
        else:
            continue
        chats[str(chat)] = text
    #print chats
    return chats

def chat_type(message):
    groupType = message['message']['chat']['type']
    return groupType

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(api_url + 'sendMessage', data=params, verify=False)
    return response

def save_active_users(fileName, chats):
    if os.access(fileName, os.F_OK) == True:
        chatsFile = open(fileName, "r")
        prevChats = json.loads(str(chatsFile.read()))
        chatsFile.close()
#        print "prevChats before"
#        print prevChats
        for key in chats.keys():
            prevChats[key] = chats[key]
        chatsFile = open(fileName, "w")
        chatsFile.write(json.dumps(prevChats))
        chatsFile.close()
    else:
        chatsFile = open(fileName, "w")
        chatsFile.write(json.dumps(chats))
        chatsFile.close()
    return chats

def chat_processing(chats):
    for key in chats.keys():
        s = chats[key]
        if s[0:4] == 'url ':
            print chats[key]
        else:
            print 'else'
            print chats[key][0:4]
    return chats
#получаем последнее сообщение в чате
updates = last_updates(get_updates_json(apiUrl))
#получаем словарь чатов и сообщений пользователя.
chats = get_chat_ids(updates)
result = chat_processing(save_active_users(activeChatsFileName, chats))
#print chat_id
#messages = get_message_texts(updates)
#print message
#send_mess(chat_id, 'Чтобы я понял тебя, мне нужна ссылка на поиск в Авито')