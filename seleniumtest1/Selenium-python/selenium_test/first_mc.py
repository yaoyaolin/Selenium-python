#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pymemcache.client.base import Client

mcache = Client(('127.0.0.1',11211))
mcache.set('say','hello,memcache',time = 100)

value = mcache.get('say')
print(value)