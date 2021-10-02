import requests

import settings

class APICallError(Exception):
    pass

class DayliSeries:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY

    def _build_url(self, path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"

    def intraday_series(self, function, symbol, outputsize, **kwargs):

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

sts = DayliSeries()

function='TIME_SERIES_DAILY';symbol='IBM';outputsize='compact'

data = sts.intraday_series(function, symbol, outputsize)

print(data)