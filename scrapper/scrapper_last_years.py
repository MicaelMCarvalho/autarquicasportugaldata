#! /usr/bin/python
"""
Entry point for scrapper module to be used in 2017 and 2013
in this module it will be defined all the logic behind the data scrapping from the website(s)
"""
import requests
import json
from .filter import Filter
from .data_transform import transform
       
class scrapper:
   def __init__(self, elections):
      self.url = {}
      self.url_votes = {}
      self.url_territorykey = {}
      self.main_territorykey = {}
      self.year = []
      for item in elections:
         self.url[item['year']] = item['url']
         self.url_votes[item['year']] = item['url_votes']
         self.url_territorykey[item['year']] = item['url_territorykey']
         self.main_territorykey[item['year']] = item['main_territorykey']
         self.year.append(item['year'])

   def _save_to_file(self, data, finename):
      with open(finename ,'w') as f:
         json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

   def start_scrapper(self):
      sort_out = Filter()
      for year in self.year:
         print(' ++++++++++ Starting Year %s ++++++++++' % (year))
         location_keys = self.get_location_key(year)
         data = self.iterateUrl(year)
         data = sort_out.get_organized_data(data, year)
         data = self.add_votes(data, location_keys, year)
         self._save_to_file(data, 'autarquicas_%s.json' % (year))
         transform.data_format_to_pandas(data, year)
         

   def iterateUrl(self, year):
      dictAllInfo = {"candidate":[]}
      for page in range(1, 100):
         print(self.url[year] % (page))
         response = requests.get(self.url[year] % (page)) 
         data = response.json()
         maxPageNum = data['numberOfPages']
         for candidate in data['electionCandidates']:
            dictAllInfo['candidate'].append(candidate)
         if page == maxPageNum:
            break
      return dictAllInfo

   def get_location_key(self, year):
      print(self.url_territorykey[year] % (self.main_territorykey[year]))
      response = requests.get(self.url_territorykey[year] % (self.main_territorykey[year]))
      data = response.json()
      dict_locations = {}
      for elem in data:
         response = requests.get(self.url_territorykey[year] % (elem['territoryKey']))
         towns = response.json()
         dict_locations[elem['name']] = {}
         dict_locations[elem['name']]['territoryKey'] = elem['territoryKey']
         dict_locations[elem['name']]['towns'] = {}
         for town in towns:
            dict_locations[elem['name']]['towns'][town['name']] = town['territoryKey']
      return dict_locations
   
   
   def get_votes(self, location_key, year):
      response = requests.get(self.url_votes[year] % (location_key))
      votes = response.json()
      return(votes['currentResults'])
   
   def add_votes(self, data, location_keys, year):
      new_data = {}
      for district in data:
         district_name = str(district)
         new_data[district_name] = {}
         for town in data[district]:
            new_data[district_name][str(data[district][town]['territoryName'])] = {}
            votes = self.get_votes(data[district][town]['territoryKey'], year)

            print('\n\n\nSTART MERGE: DISTRICT: ', data[district][town]['parentTerritoryName'], '               County:', data[district][town]['territoryName'])

            #new_data[district_name][data[district][town]['territoryName']]['candidates'] = Filter.merge_votes_with_candidates(data[district][town]['candidates'], votes)
            new_data[district_name][data[district][town]['territoryName']] = Filter.merge_votes_with_candidates(data[district][town], votes)
      return new_data

