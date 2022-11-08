import numpy as np
from sklearn.metrics import mean_absolute_error
import random as r
import scipy.stats as st
class boostraping:
    '''
    Refences:
    https://www.uvm.edu/~statdhtx/StatPages/Randomization%20Tests/BootstMedians/bootstrapping_medians.html
    '''
    def __init__(self,data:list,rows=100,k=2,func=None,alpha=.05) :
        self.data=data
        self.rows=rows
        self.k=k
        self.alpha=alpha
        self.func=func
  

    '''
    FIX Peringkasan Algoritma
    '''     
    def model_resample(self):
        if self.func==None:
            raise ValueError ('bang kamu lupa masukin parameter function')
        dummy_1=[]
        true_value=np.repeat((self.func(self.data)),self.rows)
        print('Start Bootstarp'.center(30,'='))
        for a in range(self.rows):
            dummy_2=[]
            for b in range(self.k):
                dummy_2.append(r.sample(self.data,1))
            formula=self.func(dummy_2) # point terpenting
            dummy_1.append(formula)
        mean_funct_resample=np.mean(dummy_1)
        var_mean_funct_resample=np.var(dummy_1)
        mse_mean_funct_resample=mean_absolute_error(dummy_1,true_value)
        ci_resample=[np.mean(self.data)-st.norm.ppf(1-self.alpha/2)*var_mean_funct_resample**.5,np.mean(self.data)+st.norm.ppf(1-self.alpha/2)*var_mean_funct_resample**.5]
        print('End Bootstarp'.center(30,'='))
        return dummy_1,mean_funct_resample,var_mean_funct_resample,mse_mean_funct_resample,ci_resample

def jackknife_stat(data,func,convince=.95):
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
    estimate = stat_data - bias

    z_score = np.sqrt(2.0)*erfinv(convince)
    convince = estimate + z_score*np.array((-std_err, std_err))

    return estimate, bias, std_err, convince


    
    