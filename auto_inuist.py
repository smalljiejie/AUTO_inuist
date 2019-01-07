#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import json
import base64
import re
import os
import shutil

url = 'http://10.255.255.13/index.php/index/login'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
referer = 'http://10.255.255.13'
origin = 'http://10.255.255.13'
first_use = 1
username = input("Enter your username: 学号或手机号\n")
domain = input("Enter your domain: 选填ChinaNet\\Unicom\\CMCC\\NUIST\n")
password = base64.b64encode(str.encode(input("Enter your password: \n")))
enablemacauth = '0'
login_data = parse.urlencode([
    ('username', username),
    ('password', password),
    ('domain', domain),
    ('enablemacauth', enablemacauth)
])
req = request.Request(url)
req.add_header('Origin', origin)
req.add_header('User-Agent', user_agent)
req.add_header('Referer', referer)
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
if first_use:
    shutil.copy2(os.getcwd()+'/auto_inuist.py',os.getcwd()+'/auto_inuist_tmp.py')
    f = open(os.getcwd()+'/auto_inuist.py', mode='r')
    w = open(os.getcwd()+'/auto_inuist_tmp.py', mode='w')
    for line in f:
        w.write(line.replace('username = input("Enter your username: 学号或手机号\\n")', 'username = \''+username+'\''), \
        line.replace('domain = input("Enter your domain: 选填ChinaNet\\\\Unicom\\\\CMCC\\\\NUIST\\n")', 'domain = \''+domain+'\''), \
        line.replace('password = base64.b64encode(str.encode(input("Enter your password: \\n")))', 'password = \''+password.decode()+'\''), \
        line.replace('first_use = 1', 'first_use = 0'))
    f.close()
    w.close()
os.remove(os.getcwd()+'/auto_inuist.py')
os.rename(os.getcwd()+'/auto_inuist_tmp.py', os.getcwd()+'/auto_inuist.py')