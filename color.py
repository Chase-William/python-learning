from email.policy import default
from enum import Enum

WARM_COLOR_STR = 'warm'
COLD_COLOR_STR = 'cold'
NEUTRAL_COLOR_STR = 'neutral'

class Color(Enum):
  RED = 0
  ORANGE = 1
  YELLOW = 2
  GREEN = 3
  BLUE = 4
  INDIGO = 5
  VIOLET = 6

def get_warmth(color: Color) -> str:
  # Python 3.10, they added pattern matching, very similar to Kotlin, little different from C#
  # I tried using commas instead of vertical pipe operator and it compiled, but always resulted in default
  match color:
    case Color.RED | Color.YELLOW | Color.ORANGE:
      return WARM_COLOR_STR
    case Color.BLUE | Color.INDIGO | Color.VIOLET:
      return COLD_COLOR_STR
    # Python's default case statement
    case _:
      return NEUTRAL_COLOR_STR