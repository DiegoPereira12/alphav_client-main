from decouple import config

APIKEY = config("APIKEY")
BASE_URL = config("BASE_URL", "//https://www.alphavantage.co/query")
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo