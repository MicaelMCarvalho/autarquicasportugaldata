#! /usr/bin/python
"""
Entry point for scrapper module to be used in 2017 and 2013
in this module it will be defined all the logic behind the data scrapping from the website(s)
"""
import requests
import json

       
class Scrapper:
   def __init__(self, year, url):
      self.year = year
      self.url = url


   def iterateUrl(self):
      dictAllInfo = {"candidate":[]}
      i = 1
      try:
         while True:
            print(i)
            response = requests.get(self.url % (i)) 
            data = response.json()

            maxPageNum = data['numberOfPages'] #TODO: Lazy set range
            for candidate in data['electionCandidates']:
               dictAllInfo['candidate'].append(candidate) 
         
            with open('all_candidates_%s.json'%(self.year),'w',encoding='utf-8') as file:
               json.dump(dictAllInfo,file,indent=2,ensure_ascii=False)        
            i +=1
      except :
         return

         