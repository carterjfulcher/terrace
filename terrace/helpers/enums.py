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

wait_times = {
  Frequency.TICK: 0,
  Frequency.SECOND: 1,
  Frequency.MINUTE: 60,
  Frequency.HOUR: 3600,
  Frequency.DAY: 86400,
  Frequency.WEEK: 604800,
  Frequency.MONTH: 2629743,
  Frequency.QUARTER: 7889229,
  Frequency.YEAR: 31556926
}
