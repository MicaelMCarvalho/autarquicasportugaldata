#! /usr/bin/python
import json
from scrapper import scrapper_last_years, filter

def file_exists(filename):
   try:
      f = open(filename)
      f.close()
      return True
   except IOError:
      print("%s does not exist." % (filename))
      return False


def scrapper():
   elections = open('elections.json', 'r')
   elections = json.load(elections)
   scrap = scrapper_last_years.scrapper(elections)
   scrap.start_scrapper()

  
def main():
   scrapper()


if __name__ == "__main__":
   main()
