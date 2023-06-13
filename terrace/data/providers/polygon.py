from terrace.data.providers import Provider, field
from pydantic import validate_arguments 


class Polygon(Provider):
  @validate_arguments
  def __init__(self, api_key: str):
    self.api_key = api_key
    self.name = "Polygon"
    super().__init__()
  
  """ Equities """

  """ Options """
  @field(name = 'options', description='', type='DataFrame')
  def get_options(self, underlying_ticker: str, expiration_date: str = None, contract_type: str = None):
    print("hello")
    print(self.fields)

if __name__ == "__main__":
  x = Polygon("test")
  print(x.fields)
  x.get_options("AAPL")
  