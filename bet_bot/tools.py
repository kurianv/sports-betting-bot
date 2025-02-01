def toDecimals(num):
  dec = 0

  if str(num)[0] == "-":
    dec = 1 + (100/(num*-1))
  else:
    dec = 1 + (num/100)
  return round(dec, 2)


def toAmerican(num):
  out = 0
  if num >= 2.00:
    out = (num - 1) * 100
  else:
    out = -(100/(num - 1))
  return round(out)

def arbi(out1, out2):
  total = (1/(out1)) + (1/(out2))
  return round(total, 4)

def betValue(odds, total):
  stake = 100.00
  outcome = (stake * (1/odds))/total

  return round(outcome, 2)

