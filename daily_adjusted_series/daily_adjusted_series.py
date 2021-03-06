import requests

import settings

class APICallError(Exception):
    pass

class DayliAdjustedSeries:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY

    def _build_url(self, path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"

    def dayli_adjusted_series(self, function, symbol, outputsize, **kwargs):

        path = f"function={function}&symbol={symbol}&outputsize={outputsize}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)

        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()
            
        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

sts = DayliAdjustedSeries()

function='TIME_SERIES_DAILY_ADJUSTED';symbol='IBM';outputsize='full'

data = sts.dayli_adjusted_series(function, symbol, outputsize)

print(data)