#! /usr/bin/python
"""
Entry point for scrapper module to be used in 2017 and 2013
in this module it will be defined all the logic behind the data scrapping from the website(s)
"""
import requests
import json

       
class scrapper:
   def __init__(self, year, url):
      self.year = year
      self.url = url

   def iterateUrl(self):
      dictAllInfo = {"candidate":[]}

      for link in range(1, 29):
         response = requests.get(self.url % (link)) 
         data = response.json()
         maxPageNum = data['numberOfPages'] #TODO: Lazy set range
         for candidate in data['electionCandidates']:
            #$candidates_obj = json.loads(candidates.encode('utf-8'))
            dictAllInfo['candidate'].append(candidate)
            #print(candidate['parentTerritoryName'])#candidates_obj['parentTerritoryName'], candidates_obj['territoryName'] , candidates_obj['candidates'] )
      
         with open('all_candidates_%s.json'%(self.year),'w',encoding='utf-8') as file:
            json.dump(dictAllInfo,file,indent=2,ensure_ascii=False)