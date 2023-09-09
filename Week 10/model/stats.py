from model.math import *
from random import random
def random_uniform(low : int|float,
                   high : int|float,
                   size:int=None):
    if size == None:
        return low + (high - low) * random()
    if size < 0:
        raise ValueError("size can't be 0 or blank")
    # this is for saving value iterable
    memo :list =[]
    for i in range(size):
        result =low +(high -low) * random()
        memo.append(result)
    return memo    
