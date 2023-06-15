from pydantic import BaseModel
from typing import Callable
class Field(BaseModel):
  name: str
  type: str
  description: str
  provider: str
  function: Callable
