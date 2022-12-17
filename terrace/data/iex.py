from .main import DataSource
from typing import List, Tuple
from terrace.types import Frequency
from ..index.component import IndexComponent
import pyEX
import os

class IEXDataSource(DataSource):
  def __init__(self, token: str = None, base_url: str = "https://cloud.iexapis.com/stable/stock"):
    if 'iex_token' in os.environ:
      token = os.environ['iex_token']
    
    if not token:
      raise ValueError("IEX API token not provided")
    self.api_key = token
    self.base_url = base_url 
    self._client = pyEX.Client(api_token=token, version="stable")
    self.prev = {}
  
  def _checkPriceUpdate(self, component: IndexComponent, quote: float, change: float) -> bool:
    res = (quote, change)
    if component.identifier in self.prev.keys():
      if self.prev[component.identifier] == res:
        return False
    
    self.prev[component.identifier] = res
    return True
    


  def fetchSpotPrice(self, component: IndexComponent) -> Tuple[float, float]:
    df = self._client.quote(component.identifier)
    if (realtime_quote := df['close']):
      res = realtime_quote, df['changePercent']
      if self._checkPriceUpdate(component, *res):
        return res
      else:
        return realtime_quote, 0
    else: 
      res = df['previousClose'], df['changePercent']
      if self._checkPriceUpdate(component, *res):
        return res
      return realtime_quote, 0