from model.math import *
from random import random
def random_uniform(low,high,size=None):
    if size==None:
        return low+(high-low)*random()
    if size<0:
        raise ValueError('size not in real number on negative')
    memo=[]# memory
    for i in range(size):
        result=low+(high-low)*random()
        memo.append(result)
    return (memo)    