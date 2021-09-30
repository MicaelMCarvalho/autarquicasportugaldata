import pandas as pd
import json

class transform:
    def __init__(self):
        pass

    def data_format_to_pandas(data, year):
        new = {
            "district": 
            {
            }
        }
        for entry in data:
            print(entry)
            district = str(entry)
            new['district'][district] = {
                "county":
                {
                }
            }
            for county in data[entry]:
                new['district'][district]['county'][str(county)] = data[entry][county]

        with open('autarquicas_%s_pandas,json' % (year) ,'w') as f:
            json.dump(new, f, sort_keys=True, indent=4, ensure_ascii=False)