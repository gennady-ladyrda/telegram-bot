#!/usr/bin/env python
#coding:utf-8
import ConfigParser
import requests

conf = ConfigParser.RawConfigParser()
conf.read("../../../moskal-bot.conf")
print conf.get("general", "token")
token = conf.get("general", "token")

url = "https://api.telegram.org/bot"+token+"/"

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params, verify=False)
    return response

send_mess(-282988545, 'Тебе пишет папин бот.')