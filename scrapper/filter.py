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


    def _add_entry(self, data, entry, year):
        for elem in entry['candidates']:
            try:
                elem.pop('url')
                elem.pop('alternateCandidates')
                elem.pop('imageKey')
                elem.pop('mandates')
                elem.pop('presidents')
            except:
                pass
        try:
            data[entry['parentTerritoryName']][entry['territoryName']] = entry
        except:
            data[entry['parentTerritoryName']] = {}
            data[entry['parentTerritoryName']][entry['territoryName']] = entry
            pass
        return data


    def get_organized_data(self, data, year):
        result = {}
        for entry in data['candidate']:
            result = self._add_entry(result, entry, year)

        return result

    def merge_votes_with_candidates(data, votes):
        new_data = dict(data)
        print('data id:', id(data), 'new_data id:', id(new_data))
        for candidate in new_data['candidates']:
            for entry in votes['resultsParty']:
                if entry['acronym'] == candidate['party']:
                    candidate['votes'] = {} 
                    candidate['votes'] = entry 
                    try:
                        candidate['votes'].pop('imageKey')
                    except:
                        pass
            
            new_data['total_votes'] = {
                "availableMandates": votes["availableMandates"],
                "blankVotes": votes["blankVotes"],
                "blankVotesPercentage": votes["blankVotesPercentage"],
                "displayMessage": votes["displayMessage"],
                "hasNoVoting": votes["hasNoVoting"],
                "nullVotes": votes["nullVotes"],
                "nullVotesPercentage": votes["nullVotesPercentage"],
                "numberParishes": votes["numberParishes"],
                "numberVoters": votes["numberVoters"],
                "percentageVoters": votes["percentageVoters"],
            }
        return new_data