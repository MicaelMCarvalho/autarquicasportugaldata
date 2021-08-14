#! /usr/bin/python
import json
from scrapper import scrapper_last_years
from mining import mining

def file_exists(filename):
   try:
      f = open(filename)
      f.close()
      return True
   except IOError:
      print("%s does not exist." % (filename))
      return False

def load_candidates(filename):
   with open(filename,'r') as f:
      return json.load(f)

def set_scrapper():
   #TODO add structure with all the years with elections. Grouping by url.
   # In dev , we will use only one year
   load_candidates('elections.json')
   for year in elections:
      if year['year'] in ['2017']:
         #if file_exists('all_candidates_%s.json' % (year['year'])):
         scrap = scrapper_last_years.Scrapper(year['year'], year['url'])
   return scrap
  
   
def main():
   #TODO Set option to choose between scrapp and mining
   # Dev phase, only scrapper
   #scrap = set_scrapper()
   #scrap.iterateUrl()

   tua_mae = load_candidates('all_candidates_2017.json')
   candidates_de_coimbra = mining.Mining("Coimbra",tua_mae).get_candidate_by_conselho()

   print (candidates_de_coimbra)



if __name__ == "__main__":
   main()
