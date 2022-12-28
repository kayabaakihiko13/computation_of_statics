import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli
import random as r

def pmf(data,p,size):
    # f=p**r.choice(x)*(1-p)**(1-x)
    # return f
    memo=[]
    for _ in range(size):
        x=r.choice(data)
        formula=p**x*(1-p)**(1-x)
        memo=np.append(memo,formula)
    return memo

def rvs_bernoulli(p,size=1):
    if size<=0:
        raise Exception('Can\'t size low equal than 0')
    memo=np.array([])
    for _ in range(0,size):
        if np.random.randn()<=p:
            value=1
            memo.append(value)
        else:
            value=0            
            memo.append(value)
    return memo

# gambar bar
lst=[1,2,3,4,5,2]
meta=pmf(lst,0.2,len(lst))
gambar=plt.bar(lst,meta)
st.write(gambar)


