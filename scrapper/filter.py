#! /usr/bin/python
"""
Filter the data and return a json and save it also to the file. 
The data will be organize by district and county
"""
import json

class Filter:
    def __init__(self, ):
        pass

    def _file_manager(self):
        f = open(self.filepath, 'r')
        data = json.load(f)
        f.close()
        return data


    def _save_to_file(self, data):
        with open('organized_%s' % (self.filepath) ,'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)


    def _add_entry(self, data, entry):
        president = ''

        for elem in entry['candidates']:
            elem.pop('url')
            if int(elem['presidents']) == 1: 
                president = elem['effectiveCandidates']
        result = { 'candidates': entry['candidates'], 'president': president}
        
        try:
            data[entry['parentTerritoryName']][entry['territoryName']] = result
        except:
            data[entry['parentTerritoryName']] = {}
            data[entry['parentTerritoryName']][entry['territoryName']] = result
            pass
        return data


    def get_organiz_data(self, filepath):
        self.filepath = filepath
        data = self._file_manager()
        result = {}
        for entry in data['candidate']:
            result = self._add_entry(result, entry)
        self._save_to_file(result)