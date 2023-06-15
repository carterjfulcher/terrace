from terrace.data.providers import Provider 
import warnings
from terrace.data import Field
from pydantic import validate_arguments 
from time import sleep
import os, requests
from typing import List, Optional
import pandas as pd 


class Polygon(Provider):
  @validate_arguments
  def __init__(self, api_key: str = None, cache: bool = False):
    self._api_key = os.environ.get("POLYGON_API_KEY", api_key)
    self._retries = 0
    self.name = "polygon"
    self.fields = [
      Field(name="options", description="get all options tickers for a security", type="DataFrame", function=self.get_options, provider=self.name),
      Field(name="options_aggregates", description="get aggregate options prices for a (options) ticker", type="DataFrame", function=self.get_options_aggregates, provider=self.name),
      Field(name="daily_open_close", description="get daily open/close prices for a (options) ticker", type="DataFrame", function=self.get_options_daily_open_close, provider=self.name)
    ]
    self._base = "https://api.polygon.io"
    super().__init__(cache=cache)

  def _request(self, path: str):
    url = f"{self._base}{path}&apiKey={self._api_key}"
    response = requests.get(url).json()
    if(response['status'] == 'ERROR'):
      print(response)
      print(f"warning: rate limit error was encountered...waiting and retrying in {2 ** self._retries}s...")
      sleep(2 ** self._retries)
      self._retries += 1
      response = self._request(path)
    self._retires = 0
    return response
  
  """ Equities """

  """ Options """
  def get_options(self, underlying_ticker: str, contract_type: str = None, expiration_date: str = None): 
    path = f"/v3/reference/options/contracts?underlying_ticker={underlying_ticker}"
    if contract_type is not None:
      path += f"&contract_type={contract_type}"
    if expiration_date is not None:
      path += f"&expiration_date={expiration_date}"
    contracts = []
    while path is not None:
      response = self._request(path)
      contracts += response['results']
      try:
        path= f"{response['next_url']}".replace(self._base, '')
      except KeyError:
        path = None
    return pd.DataFrame(contracts)
  
  def get_options_aggregates(self, ticker: str, multiplier: int = 1, timespan: str = "day", from_: str = None, to: str = None, limit: int = 5000):
    if from_ is None:
      raise ValueError("from_ must be specified")
    if to is None:
      raise ValueError("to must be specified")
    path = f"/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_}/{to}?limit={limit}"
    response = self._request(path)
    return pd.DataFrame(response['results'])
  
  def get_options_daily_open_close(self, ticker: str, date: str, adjusted: bool = True):
    path = f"/v1/open-close/{ticker}/{date}?adjusted={adjusted}"
    response = self._request(path)
    return response

if __name__ == "__main__":
  x = Polygon()
  price = x.get_options_daily_open_close("O:AAPL230616C00162500", "2023-06-13")

  