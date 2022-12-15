from dataclasses import dataclass
from typing import List, Any
import pandas as pd 
import numpy as np

@dataclass
class IndexComponent:
  identifier: str 
  weight: float
  _data: dict = None 

  # make values from _data available as attributes
  def __getattribute__(self, __name: str) -> Any:
    if __name == "_data":
      return super().__getattribute__("_data")
    elif __name in self._data:
      return self._data[__name]
    else:
      return super().__getattribute__(__name)


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
  def fromCsv(self, path: str):
    return self.__process_dataframe(pd.read_csv(path))

  @classmethod
  def fromExcel(self, path: str):
    with open(path ,mode="rb") as excel_file:
      df = pd.read_excel(excel_file)
      return self.__process_dataframe(df)