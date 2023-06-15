from terrace import Strategy
from terrace.data import Context, Polygon
from terrace.trading import Engine 
from datetime import timedelta

class WheelStrategy(Strategy):
  def step(self, ctx: Context):
    closest_friday_date = ctx.time + timedelta(days=4 - ctx.time.weekday())
    options = ctx.polygon.get_options("BIBL", "call", closest_friday_date.strftime("%Y-%m-%d"))
    print(options)
    for index, row in options.iterrows():
      price = ctx.polygon.get_options_daily_open_close(row['ticker'], (ctx.time - timedelta(1)).strftime("%Y-%m-%d"))
      print(price)
      break

if __name__ == "__main__":
  wheel = WheelStrategy()
  context = Context(Polygon())
  Engine(wheel, context).run()
