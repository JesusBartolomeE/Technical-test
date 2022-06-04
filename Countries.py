from hashlib import sha1
import requests
import time

class Countries:

    def __init__(self,region = 'Africa'):
        self._region = region
        self._start = None
        self._end = None

    def get_lenguages(self,name_countrie):
        try:
            self._start = time.time()
            res = requests.get(f'https://restcountries.com/v3.1/region/{self._region}')
            countries = res.json()
            lenguages = None
            for countrie in countries:
                if countrie['name']['common'] == name_countrie:
                    lenguages = list(countrie['languages'].values())
            return {
                "Región":self._region,
                "City Name":name_countrie,
                "Language":self._encript_lenguages(lenguages),
                "Time":self._end-self._start
            }
        except Exception as e:
            return {
                "error": e
            }    

    def _encript_lenguages(self,lenguages):
        lenguages= bytes(f'{lenguages}','utf-8')
        hash_object =sha1(lenguages).hexdigest()
        self._end=time.time()
        return hash_object
