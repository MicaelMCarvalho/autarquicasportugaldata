#! /usr/bin/python
import json
from scrapper import scrapper_last_years

def file_exists(filename):
   try:
      f = open(filename)
      f.close()
      return True
   except IOError:
      print("%s does not exist." % (filename))
      return False


def set_scrapper():
   #TODO add structure with all the years with elections. Grouping by url.
   # In dev , we will use only one year
   elections = open('elections.json', 'r')
   elections = json.load(elections)
   for year in elections:
      if year['year'] in ['2017']:
         #if file_exists('all_candidates_%s.json' % (year['year'])):
         scrap = scrapper_last_years.Scrapper(year['year'], year['url'])
   return scrap
  
   
def main():
   #TODO Set option to choose between scrapp and mining
   # Dev phase, only scrapper
   scrap = set_scrapper()
   scrap.iterateUrl()


if __name__ == "__main__":
   main()
