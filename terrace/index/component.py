from dataclasses import dataclass
from typing import List, Dict
import pandas as pd 
import numpy as np

@dataclass
class IndexComponent:
  identifier: str 
  weight: float
  _data: dict = None

  def __getitem__(self, __name):
    if __name in self.__dict__.keys():
      return self.__dict__[__name]
    return self._data[__name]

  @classmethod 
  def fromList(self, list: List[str]):
    return [IndexComponent(identifier, 1 / len(list)) for identifier in list]

  def __process_dataframe(dataframe: pd.DataFrame):
    print("Processing data...")
    components = []
    records = dataframe.to_dict("records")
    for record in records:
      i = IndexComponent(record[list(record.keys())[0]], 1 / len(records), record)
      if i.identifier != np.nan: components.append(i)
    return components

  @classmethod 
  def fromCsv(self, path: str) -> List:
    return self.__process_dataframe(pd.read_csv(path))

  @classmethod 
  def fromDataFrame(self, df: pd.DataFrame) -> List:
    return self.__process_dataframe(df)

  @classmethod
  def fromExcel(self, path: str) -> List:
    with open(path ,mode="rb") as excel_file:
      df = pd.read_excel(excel_file)
      return self.__process_dataframe(df)
  
  @classmethod 
  def fromRecords(self, list: List[Dict], identifier_key: str):
    return [IndexComponent(record[identifier_key], 1 / len(list)) for record in list]