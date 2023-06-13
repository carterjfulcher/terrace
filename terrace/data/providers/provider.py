from terrace.data import Field 
from typing import List
from functools import wraps

def field(name: str = None, type: str = None, description: str = None):
  def _impl(f):
    def wrapper(self, *args, **kwargs):
      self.fields.append(Field(name=name, type=type, description=description, provider=self.name))
      return f(self, *args, **kwargs)
    return wrapper
  return _impl

class Provider:
  def __init__(self):
    self.fields: List[Field] = []

  