from terrace.data.providers import Provider
from terrace.data import Field 
import pandas as pd 
from pydantic import validate_arguments
from pydantic.fields import Optional
from typing import List

class FileProvider(Provider):
  @validate_arguments
  def __init__(self, filename: str, index: Optional[str] = None, columns: Optional[List[str]] = None, name: Optional[str] = "CSV"):
    self.filename = filename
    self.index = index
    self.name = name 
    self.columns = columns
    super().__init__()

  def _load(self, df: pd.DataFrame):
    if self.columns == None:
      self.columns = df.columns
    for col in [i for i in [*self.columns, self.index] if i is not None]:
      if col not in df.columns:
        raise ValueError(f"Column {col} not found in {self.filename}")
    if self.index is not None:
      self.df.set_index(self.index, inplace=True)
    if self.columns is not None:
      self.df = df[self.columns]
    else:
      self.df = df
    self._load_fields_from_df()

  def _load_csv(self):
    self._load(pd.read_csv(self.filename))

  def _load_excel(self):
    self._load(pd.read_excel(self.filename))

  def _load_fields_from_df(self):
    for col in self.df.columns:
      self.fields.append(Field(name=col, type=self.df[col].dtype.name, description="", provider=self.name))

class CSV(FileProvider):
  def __init__(self, filename: str, index: Optional[str] = None, columns: Optional[List[str]] = None):
    super().__init__(filename, index, columns)
    self._load_csv()

class Excel(FileProvider):
  def __init__(self, filename: str, index: Optional[str] = None, columns: Optional[List[str]] = None):
    super().__init__(filename, index, columns)
    self._load_excel()
