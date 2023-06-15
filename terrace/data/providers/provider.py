from terrace.data import Field 
from typing import List
from functools import wraps

class Provider:
  def __init__(self, cache = False):
    self._cache = cache
    self.fields: List[Field] = []

  