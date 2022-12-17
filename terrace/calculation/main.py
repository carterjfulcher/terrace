from ..index import Index 
from ..data import DataSource
from ..types import Frequency
import time 


class CalculationEngine:
  def __init__(self, data_source: DataSource): 
    self._data_source = data_source

  def start(self, index: Index, frequency: Frequency):
    while True:
      index._calculate(self._data_source)
      time.sleep(frequency.value[0])
