
from random import random
import time as t
import numpy as np
from sklearn.metrics import mean_absolute_error
import random as r
import scipy.stats as st

def boostraping(data:list,rows=100,k=2,func=None,alpha=.05):
        start=t.time()
        if func==None:
            raise ValueError ('bang kamu lupa masukin parameter function')
        dummy_1=[]
        true_value=np.repeat((func(data)),rows)
        print('Start  Bootstarp'.center(30,'='))
        for a in range(rows):
            dummy_2=[]
            for b in range(k):
                dummy_2.append(r.sample(data,1))
            formula=func(dummy_2) # import point
            dummy_1.append(formula)
        mean_funct_resample=np.mean(dummy_1)
        var_bootstraping=np.var(dummy_1)
        mse_mean_funct_resample=mean_absolute_error(dummy_1,true_value)
        ci_resample=[np.mean(data)-st.norm.ppf(1-alpha/2)*var_bootstraping**.5,np.mean(data)+st.norm.ppf(1-alpha/2)*var_bootstraping**.5]
        print(t.time()-start)
        print('End Bootstarp'.center(30,'='))
        return dummy_1,mean_funct_resample,var_bootstraping,mse_mean_funct_resample,ci_resample

def jackknife_stat(data,func,convince=.95):
    """
    data,this parameter is sampling
    func,this parameter for your mean are you mean
    convince,this parameter value true zscore 
    """
    "Data its Resample"
    '''
    Full Refence:
    https://docs.astropy.org/en/stable/api/astropy.stats.jackknife_stats.html
    https://docs.astropy.org/en/stable/_modules/astropy/stats/jackknife.html#jackknife_stats
    '''

    dummy=data.copy()
    dummy=np.array(dummy)
    n=dummy.shape[0]
    resamples = np.empty([n, n-1])
    for i in range(n):
        resamples[i] = np.delete(data, i)

    if func==None:
        raise ValueError('Lupa masukin functionnya')
    
    if not (0<convince<1):
        raise ValueError('tidak bisa')

    if n<=0:
        raise ValueError('data must contain at least one measurement.')

    # import erfinv
    from scipy.special import erfinv
    stat_data = func(data)
    jack_stat = np.apply_along_axis(func, 1, resamples)
    mean_jack_stat = np.mean(jack_stat, axis=0)
    bias = (n-1)*(mean_jack_stat - stat_data)
    std_err = np.sqrt((n-1)*np.mean((jack_stat - mean_jack_stat)*(jack_stat -
                                        mean_jack_stat), axis=0))
    variance=np.var(resamples)
    estimate = stat_data - bias
    z_score = np.sqrt(2.0)*erfinv(convince)
    convince_interval = estimate + z_score*np.array((-std_err, std_err))
    
    return resamples,estimate,variance,bias, std_err,convince_interval
# for number 3
def random_uniform(low=0,high=1,size=None):
    if size==None:
        return low+(high-low)*random()
    if size<0:
        raise ValueError('size not in real number on negative')
    memo=[]# memory
    for i in range(size):
        result=low+(high-low)*random()
        memo.append(result)
    return (memo)    

class bernoulli:

    def pmf(x,p):
        f=p**x*(1-p)**(1-x)
        return f
