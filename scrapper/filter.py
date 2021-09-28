#! /usr/bin/python
"""
Filter the data and return a json and save it also to the file. 
The data will be organize by district and county
"""
import json

class Filter:
    def __init__(self):
        pass

    def _file_manager(self):
        f = open(self.filepath, 'r')
        data = json.load(f)
        f.close()
        return data


    def _save_to_file(self, data, year):
        with open('autarquicas_%s.json' % (year) ,'w') as f:
            json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

    def _add_entry(self, data, entry):
        for elem in entry['candidates']:
            print(elem)
            try:
                elem.pop('url')
                elem.pop('alternateCandidates')
            except:
                pass
        #result = { 'candidates': entry['candidates'], 'president': president}
        
        try:
            data[entry['parentTerritoryName']][entry['territoryName']] = entry['candidates']
        except:
            data[entry['parentTerritoryName']] = {}
            data[entry['parentTerritoryName']][entry['territoryName']] = entry['candidates']
            pass
        return data

    def get_organized_data(self, data, year):
        #data = self._file_manager()
        result = {}
        for entry in data['candidate']:
            result = self._add_entry(result, entry)
        self._save_to_file(result, year)