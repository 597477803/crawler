#!/bin/python 2.7 
# -*- coding:gbk -*-

import requests
import traceback

def download(url):
    content = ""
    try:
        content = request.get(url).content
    except:
        traceback.print_exc()
    return content
