#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import redis
from datetime import datetime
ONLINE_LAST_MINUTES=5

redis = redis.Redis()
def mark_online(user_id):
    now = int(time.time())
    expires = now + (app.config['ONLINE_LAST_MINUTES']*60)+10
    all_users_key = 'online-users/%d'%(now//60)
    user_key = 'user-activity/%s'%user_id
    p = redis.pipeline()
    p.sadd(all_users_key,user_id)
    p.set(user_key,now)
    p.expireat(all_users_key,expires)
    p.expireat(user_key,expires)
    p.execute()

def get_user_last_activity(user_id):
    last_active = redis.get('user-activity/%s'%user_id)
    if last_active is None:
        return None
    return datetime.utcfromtimestamp(int(last_active))

def get_online_users():
    current = int(time.time())
    minutes = xrange(app.config['ONLINE_LAST_MINUTES'])
    return redis.sunion(['online-users/%d'%(current-x) for x in minutes])

s = get_online_users()
print(s)

