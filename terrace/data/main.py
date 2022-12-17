from typing import List, Tuple
from ..index.component import IndexComponent

""" Template for DataSources"""
class DataSource:
  def fetch_price(self, component: IndexComponent) -> Tuple[float, float]:
    pass 

  def fetch_price_bulk(self, components: List[IndexComponent]):
    pass