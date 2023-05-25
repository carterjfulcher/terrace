from enum import Enum

class Frequency(Enum):
  TICK = 0,
  SECOND = 1,
  MINUTE = 2,
  HOUR = 3,
  DAY = 4,
  WEEK = 5,
  MONTH = 6,
  QUARTER = 7,
  YEAR = 8

class Strategy:
  """
  Strategies contains the logic for evaluating context and creating orders ONLY. Should always remain ambiguous to the broker and target asset

  This class in particular templates the methods of a strategy. 

  """

  def __init__(self, 
    frequency: Frequency = Frequency.DAY):
    frequency: Frequency = frequency

  def on_tick(self, tick):
    pass

  def on_start(self):
    pass

  def on_end(self):
    pass

  def on_market_open():
    pass

  def on_market_close():
    pass
