"""

Strategy

"""
from terrace.strategy import Strategy, on_tick
from terrace.strategy.tools import ta

class TAStrategy(Strategy):
  @Strategy.on_tick
  def handle_tick(self, ctx):
    sma = ta.sma(ctx.close, 20)
    if ctx.close > sma:
      self.long()
    elif ctx.close < sma:
      self.short()

"""

Live Trading

"""
from terrace.broker import Alpaca
from terrace.engine import Engine 

broker = Alpaca(api_key="", secret_key="")
engine = Engine(
  broker=broker,
  strategy=TAStrategy,
)

engine.execute()

"""

Back Testing

"""

