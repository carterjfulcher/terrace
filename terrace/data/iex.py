from .main import DataSource
from typing import List
from index.component import IndexComponent

class IEXDataSource(DataSource):
  def __init__(self, api_key: str, base_url: str = "https://cloud.iexapis.com/stable/stock"):
    self.api_key = api_key
    self.base_url = base_url 

  def fetch_price(self, component: IndexComponent):
    pass

  def fetch_price_bulk(self, components: List[IndexComponent]):
    pass