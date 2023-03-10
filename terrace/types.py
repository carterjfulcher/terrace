from enum import Enum 

class IndexType(Enum):
  PRICE_RETURN = 0, 
  GROSS_TOTAL_RETURN = 1,
  NET_TOTAL_RETURN = 2,

class Frequency(Enum):
  THREE_SECONDS = 3,
  FIFTEEN_SECONDS = 15,
  THIRTY_SECONDS = 30,
  MINUTELY = 60,
  HOURLY = 3600,
  DAILY = 86400,
  WEEKLY = 604800,
  MONTHLY = 2592000,
  QUARTERLY =  7776000,
  YEARLY = 31536000,

class WeightingMethod(Enum):
  EQUAL_WEIGHT = 0,
  MARKET_CAP_WEIGHT = 1,
  CUSTOM_WEIGHT = 2,
