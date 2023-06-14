from terrace.data.providers import Provider, field
from pydantic import validate_arguments 
from time import sleep
import os, requests
from typing import List 
import pandas as pd 


class Polygon(Provider):
  @validate_arguments
  def __init__(self, api_key: str = None):
    self._api_key = os.environ.get("POLYGON_API_KEY", api_key)
    self._retries = 0
    self._base = "https://api.polygon.io"
    self.name = "Polygon"
    super().__init__()

  def _request(self, path: str):
    print("Hello")
    url = f"{self._base}{path}&apiKey={self._api_key}"
    response = requests.get(url).json()
    if(response['status'] == 'ERROR'):
      if response['error'] == "You've exceeded the maximum requests per minute, please wait or upgrade your subscription to continue. https://polygon.io/pricing":
        print("error was encountered...waiting and retrying...")
        sleep(2 ** self._retries)
        self._retries += 1
        response = self._request(path)
      else:
        raise ValueError(f"Error encountered: {response['error']}")
    self._retires = 0
    return response
  
  """ Equities """

  """ Options """
  @field(name = 'options', description='get all options tickers for a security', type='DataFrame')
  def get_options(self, underlying_ticker: str, contract_type: str = None, expiration_date: str = None): 
    path = f"/v3/reference/options/contracts?underlying_ticker={underlying_ticker}"
    if contract_type is not None:
      path += f"&contract_type={contract_type}"
    if expiration_date is not None:
      path += f"&expiration_date={expiration_date}"
    contracts = []
    while path is not None:
      response = self._request(path)
      print(response)
      contracts += response['results']
      try:
        path= f"{response['next_url']}".replace(self._base, '')
      except KeyError:
        path = None
    return pd.DataFrame(contracts)
  
  @field(name = "options_aggregates", description="get aggregate options prices for a (options) ticker", type="DataFrame")
  def get_options_aggregates(self, ticker: str, multiplier: int = 1, timespan: str = "day", from_: str = None, to: str = None, limit: int = 5000):
    if from_ is None:
      raise ValueError("from_ must be specified")
    if to is None:
      raise ValueError("to must be specified")
    path = f"/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_}/{to}?limit={limit}"
    response = self._request(path)
    return pd.DataFrame(response['results'])
  
  @field(name = "daily_open_close", description="get daily open/close prices for a (options) ticker", type="DataFrame")
  def get_options_daily_open_close(self, ticker: str, date: str, adjusted: bool = True):
    path = f"/v1/open-close/{ticker}/{date}?adjusted={adjusted}"
    response = self._request(path)
    return response

if __name__ == "__main__":
  x = Polygon("epyXyAAEoeeoUopA7MvuWHXxr4aWJL0N")
  price = x.get_options_daily_open_close("O:AAPL230616C00162500", "2023-06-13")
  print('price: ', price)

  