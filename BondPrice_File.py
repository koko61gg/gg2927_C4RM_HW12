# getBondPrice
import numpy as np

def getBondPrice(y,face,couponRate,m,ppy):
  cf = face * couponRate / ppy # coupon
  t = np.arange(1, m * ppy + 1) # time period
  pv = (1 + y/ppy)**-(t) # discount factor
  disc_coupon = sum(cf * pv) # sum of discounted coupons
  disc_face = face * pv[-1] # discounted face
  BondPrice = disc_coupon + disc_face
  return(BondPrice)
