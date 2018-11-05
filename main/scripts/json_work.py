#!/usr/bin/env python
# coding: utf8
import json

message = []
message =  {u'message': {u'date': 1541102864, u'text': u'oh, great)', u'from': {u'username': u'Gennady_Ladyrda', u'first_name': u'G', u'last_name': u'L', u'is_bot': False, u'language_code': u'en-US', u'id': 118182323}, u'message_id': 89, u'chat': {u'username': u'Gennady_Ladyrda', u'first_name': u'G', u'last_name': u'L', u'type': u'private', u'id': 118182323}}, u'update_id': 435615465}
print message
print message ['message']['chat']['id']