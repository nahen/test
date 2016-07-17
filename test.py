#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib

def getImage(save_directory,url):
    img = urllib.request.urlopen(url)
    localfile = open(save_directory + url[url.rfind('/')+1:], 'wb')
    localfile.write(img.read())
    img.close()
    localfile.close()

save_directory = "/Users/nahen/Desktop"
url = "http://www.cafe-gentle.jp/challenge/tips/python_tips_001.html"
getImage(save_directory, url)
