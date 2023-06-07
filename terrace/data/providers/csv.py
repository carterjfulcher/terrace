from terrace.data.providers import Provider
import pandas as pd 
from pydantic import validate_arguments
from pydantic.fields import Optional
from typing import List

class FileProvider(Provider):
  @validate_arguments
  def __init__(self, filename: str, index: Optional[str] = None, columns: Optional[List[str]] = None):
    self.filename = filename
    self.index = index
    self.columns = columns

    super().__init__()

  @validate_arguments
  def _load(self, df: pd.DataFrame):
    for col in [*self.columns, self.index]:
      if col not in self.df.columns:
        raise ValueError(f"Column {col} not found in {self.filename}")

    if self.index is not None:
      self.df.set_index(self.index, inplace=True)

    if self.columns is not None:
      self.df = self.df[self.columns]
    else:
      self.df = df

  def _load_csv(self):
    self._load(pd.read_csv(self.filename))

  def _load_fields_from_df(self):
    pass

