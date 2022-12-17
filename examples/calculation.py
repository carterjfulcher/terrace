from terrace import CalculationEngine, Index, Frequency, IndexComponent
from terrace.data import IEXDataSource

def audit():
  pass

def create():
  pass

myIndex = Index(
  identifier=".TESTINDEX",
  strategy=(audit, create)
)

myIndex.components = IndexComponent.fromList(['AAPL', 'TSLA', 'MSFT', 'AMZN', 'GOOG'])


engine = CalculationEngine(IEXDataSource())
engine.start(myIndex, Frequency.THREE_SECONDS)