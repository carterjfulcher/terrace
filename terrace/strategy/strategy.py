from enum import Enum

class Frequency(Enum):
  TICK = 'tick',
  SECOND = '1s',
  MINUTE = '1m',
  HOUR = '1hr',
  DAY = '1d',
  WEEK = '1wk',
  MONTH = '1mo',
  QUARTER = '1q',
  YEAR = '1y'

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
