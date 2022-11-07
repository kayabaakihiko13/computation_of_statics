import numpy as np
from sklearn.metrics import mean_absolute_error
import random as r
import scipy.stats as st
class boostraping:
    '''
    Refences:
    https://www.uvm.edu/~statdhtx/StatPages/Randomization%20Tests/BootstMedians/bootstrapping_medians.html
    '''
    def __init__(self,data:list,rows=100,k=2,alpha=.05) :
        self.data=data
        self.rows=rows
        self.k=k
        self.alpha=alpha
    # def rata_rata(self):
    #     hasil=0
    #     count=0
    #     for a in self.data:
    #         hasil+=a
    #         count+=1
    #     hasil/=count
    #     return hasil

    '''
    masih tahap perkembangan
    '''
    # def sorting(self):
    #     new_list=[]
    #     minimum_value=self.data[0]
    #     for i in range(len(self.data)):
    #         if i < minimum_value:
    #             minimum_value=i
    #     self.data.remove(minimum_value)
    #     new_list.append(minimum_value)
    # pass
            
    def mean_bootsrap(self):
        dumm_data=sorted(self.data)
        dummy_1=[]
        mean_true=np.repeat((np.mean(self.data)),self.rows)
        print('Start Bootstarp'.center(30,'='))
        for a in range(self.rows):
            dummy_2=[]
            for b in range(self.k):
                rumbling=r.sample(self.data,1)
                dummy_2.append(rumbling)
            mean_sample=np.mean(dummy_2) # point terpenting
            dummy_1.append(mean_sample)
        mean_resample=np.mean(dummy_1)
        var_mean_resample=np.var(dummy_1)
        mse_mean_resample=mean_absolute_error(dummy_1,mean_true)
        ci_resample=[np.mean(self.data)-st.norm.ppf(1-self.alpha/2)*var_mean_resample**.5,np.mean(self.data)+st.norm.ppf(1-self.alpha/2)*var_mean_resample**.5]
        print('End Bootstarp'.center(30,'='))
        return dummy_1,mean_resample,var_mean_resample,mse_mean_resample,ci_resample
    def variance(self):
        list_1=[]
        for x in range(self.rows):
            list_2=[]
            for y in range(self.k):
                list_2.apppend(r.sample(self.data,1))
            variance=np.variance(list_2)
            var_resample=np.mean(list_1)
            return var_resample
    def median_bootrap(self):
        dummy_1=[]
        median_true=np.repeat(np.median(self.data),self.rows)
        for i in range(self.rows):
            dumm_2=[]
            for j in range(self.k):
                dumm_2.append(r.sample(self.data,1))
            median_sample=np.median(dumm_2)
            dummy_1.append(median_sample)
        mean_median_resample=np.mean(dummy_1)
        varian_med_resample=np.var(dummy_1)
        mse_var_resample=mean_absolute_error(dummy_1,median_true)
        ci_med_resample=[np.mean(self.data)-st.norm.ppf(1-self.alpha/2)*varian_med_resample**.5,np.mean(self.data)+st.norm.ppf(1-self.alpha/2)*varian_med_resample**.5]


        return dummy_1,mean_median_resample,varian_med_resample,mse_var_resample,ci_med_resample

        


        
        
        