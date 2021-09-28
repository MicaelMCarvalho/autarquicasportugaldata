#! /usr/bin/python
"""
Entry point for scrapper module to be used in 2017 and 2013
in this module it will be defined all the logic behind the data scrapping from the website(s)
"""
import requests
import json
from .filter import Filter

       
class scrapper:
   def __init__(self, elections):
      self.url = {}
      self.year = []
      for item in elections:
         self.url[item['year']] = item['url']
         self.year.append(item['year'])

   def start_scrapper(self):
      sort_out = Filter()
      for year in self.year:
         data = self.iterateUrl(year)
         data = sort_out.get_organized_data(data, year)

   def iterateUrl(self, year):
      dictAllInfo = {"candidate":[]}
      for page in range(1, 50):
         print(self.url[year] % (page))
         response = requests.get(self.url[year] % (page)) 
         data = response.json()
         maxPageNum = data['numberOfPages'] #TODO: Lazy set range
         print(maxPageNum)
         for candidate in data['electionCandidates']:
            dictAllInfo['candidate'].append(candidate)
         if page == maxPageNum:
            break
      return dictAllInfo