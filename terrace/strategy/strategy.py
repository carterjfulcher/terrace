from abc import abstractmethod, ABC
from terrace.helpers import Frequency

class Strategy(ABC):
  """
  Strategies contains the logic for evaluating context and creating orders ONLY. Should always remain ambiguous to the broker and target asset

  This class in particular templates the methods of a strategy. 

  """

  def __init__(self, 
    frequency: Frequency = Frequency.DAY):
    frequency: Frequency = frequency

  @abstractmethod
  def step(self, tick):
    pass