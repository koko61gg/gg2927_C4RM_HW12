# FizzBuzz
import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish+1)
    objvec = np.array(numvec, dtype = object)

    objvec[numvec % 3 == 0] = 'fizz'
    objvec[numvec % 5 == 0] = 'buzz'
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = 'fizzbuzz'
    objvec[(numvec % 3 != 0) & (numvec % 5 != 0)] = numvec[(numvec % 3 != 0) & (numvec % 5 != 0)]

    return objvec
