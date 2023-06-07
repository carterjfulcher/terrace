def test_strategy_creation():
    from terrace.strategy import Strategy
    from terrace.helpers import ta
    class TAStrategy(Strategy):
        def step(self, ctx):
            sma = ta.sma(ctx.close, 20)
            if ctx.close > sma:
                self.long()
            elif ctx.close < sma:
                self.short()
