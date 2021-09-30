# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:31:04 2021

@author: hp
"""
import requests
import pandas as pd

url= "https://raw.githubusercontent.com/krishnaik06/Dockers/master/TestFile.csv"
res = requests.get(url, allow_redirects= True)
with open("TestFile.csv", "wb")as file:
    
    file.write(res.content)
TestFile= pd.read_csv('TestFile.csv')    