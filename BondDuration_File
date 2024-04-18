# getBondDuration
import numpy as np

def getBondDuration(y,face,couponRate,m,ppy):
  t = np.arange(1, m * ppy + 1) # time period
  cf = face * couponRate / ppy
  pv = (1 + y/ppy)**-(t) # discount factor
  disc_coupon = sum(cf * pv)
  disc_face = face * pv[-1]
  BondPrice = disc_coupon + disc_face
  w_t = sum(cf * pv * t) + face * pv[-1] * t[-1]
  BondDuration = w_t / BondPrice

  return(BondDuration)
