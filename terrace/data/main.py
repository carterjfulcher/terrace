from typing import List
from index.component import IndexComponent

""" Template for DataSources"""
class DataSource:
  def fetch_price(self, component: IndexComponent):
    pass 

  def fetch_price_bulk(self, components: List[IndexComponent]):
    pass