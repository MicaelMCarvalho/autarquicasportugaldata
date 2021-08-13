#! /usr/bin/python
"""
Entry point for scrapper module
in this module it will be defined all the logic behind the data scrapping from the website(s)
"""
import requests
import json

       
class scrapper:
   def iterateUrl(self):
      dictAllInfo = {"candidate":[]}

      for link in range(1, 29):
         response = requests.get("https://www.eleicoes.mai.gov.pt/autarquicas2013/static-data/candidates/PARTIES-CANDIDATES-CM-PAGE-%s.json" % (link)) 
         data = response.json()
         maxPageNum = data['numberOfPages'] #TODO: Lazy set range
         for candidate in data['electionCandidates']:
            #$candidates_obj = json.loads(candidates.encode('utf-8'))
            dictAllInfo['candidate'].append(candidate)
            #print(candidate['parentTerritoryName'])#candidates_obj['parentTerritoryName'], candidates_obj['territoryName'] , candidates_obj['candidates'] )
      
         with open('all_candidates.json','w',encoding='utf-8') as file:
            json.dump(dictAllInfo,file,indent=2,ensure_ascii=False)
            

def main():
   scrap = scrapper()
   scrap.iterateUrl()    

main()    
