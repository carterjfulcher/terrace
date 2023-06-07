class TechnicalAnalysis:
  def sma(self, series, period):
    return series.rolling(period).mean()