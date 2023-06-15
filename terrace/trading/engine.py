from terrace.helpers import Frequency, wait_times
from time import sleep

class Engine:
  def __init__(self, strategy, context):
    self._strategy = strategy
    self._context = context

  def run(self, exchange = None, frequency = Frequency.DAY, target = None):
    print("passing data to strategy")
    self._strategy.step(self._context)
    print("checking if order needs to be executed")
    print("executing order")
    print(f"waiting for next tick, in {wait_times[frequency]} seconds")
    sleep(wait_times[frequency])
