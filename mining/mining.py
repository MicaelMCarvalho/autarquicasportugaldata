#! /usr/bin/python
"""
Entry Point for mining module.
In this module it will be defined all the logic behing, data analysis and results

"""

class Mining:
    def __init__(self,conselho,candidate):
        self.conselho = conselho
        self.candidate = candidate


    def get_candidate_by_conselho(self):
        return[ i for i in self.candidate['candidate'] if i.get('parentTerritoryName') == self.conselho]