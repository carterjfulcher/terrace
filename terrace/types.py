from enum import Enum 

class IndexType(Enum):
  PRICE_RETURN = 0, 
  GROSS_TOTAL_RETURN = 1,
  NET_TOTAL_RETURN = 2,

class Frequency(Enum):
  DAILY = 0,
  WEEKLY = 1,
  MONTHLY = 2,
  QUARTERLY = 3,
  YEARLY = 4,

class WeightingMethod(Enum):
  EQUAL_WEIGHT = 0,
  MARKET_CAP_WEIGHT = 1,
  CUSTOM_WEIGHT = 2,
