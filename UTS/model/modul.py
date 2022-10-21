import numpy as np
import pandas as pd
class statistic:
    # Make Module Own Mean,Median,Modus,variation,covariace and correlation
    def _mean(data:list):
        _sum=0
        count_lenght=0
        for a in data:
            _sum+=a
            count_lenght+=1
        result=_sum/count_lenght
        return result
    def mean_population(data:list):
        _sum=0
        count_lenght=-1
        for a in data:
            _sum+=a
            count_lenght+=1
        result=_sum/count_lenght
        return result
    def median_val(data):
        # first must be sorted from smallest to biggest
        """
        for paper/journal reference:
            https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/median/
        """
        data.sort_values()
        dummy=data
        n=len(data)
        index=n//2
        if n%2:
            return dummy[index]
        else:
            return sum(dummy[index - 1:index + 1])/2
        
    def _mode(data):
        # first data be sort from smallest to biggest
        # dummy data variabel
        data=data.values.tolist()
        dummy_data=[]
        index=0
        while index<len(data):
            dummy_data.append(data.count(data[index]))
            index+=1
        _combine=dict(zip(data,dummy_data))
        lst=[a for (a,b) in _combine.items() if b ==max(dummy_data)]
        result=[]
        min_value=lst[0]
        for x in lst:
            if x<min_value:
                min_value=x
        result.append(min_value)
        lst.remove(min_value)
        if result == 0:
            return "Semua item memiliki frequensi sama"
        else:
        # apabila hasilnya 0,maka hasilnya tidak ada yang banyak alias jumlah frequensy item sama banyak
            pass
        return result
    def _variation(data:list):
        """In probability theory and statistics, variance is the expectation of the squared deviation of a random variable from its population mean or sample mean. Variance is a measure of dispersion, meaning it is a measure of how far a set of numbers is spread out from their average value"""
        _sum=0
        count=0
        for a in data:
            _sum+=(a-statistic._mean(data))**2
            count+=1
        result=_sum/(count-1)
        return result
    def _cov(x:list,y:list):
        # is like _variation
        # for mean we call function _mean()
        # subtracing mean from the individual elements
        # documentation refence https://python.plain.english.io/covariance-calculation-using-python-45b6a8e5df9f
        n=len(x)
        x_sub=[i-statistic._mean(x) for i in x]
        y_sub=[i-statistic._mean(y) for i in y]
        numberic=sum([x_sub[a]*y_sub[a] for a in range(n)])
        result=numberic/(n-1)
        return result
    def _correlation(x:list,y:list):
        result=statistic._cov(x,y)/pow((statistic._variation(x)*statistic._variation(y)),0.5)
        return result
    # def std_two_pol(x,y):
    #     sub_x=sum([((i-statistic._mean(x))**2) for i in x])
    #     sub_y=sum([((j-statistic._mean(y))**2) for j in y])
    #     result=(sub_x+sub_y)/(len(x)+len(y)-2)
    #     return result
    
    def t_value_ind(x,y):
        'http://www.sthda.com/english/wiki/t-test-formula'
        'https://vitalflux.com/two-sample-t-test-formula-examples/#:~:text=The%20two%20sample%20t%2Dstatistic,two%20data%20sets%20(H0).'
        atas=statistic._mean(x)-statistic._mean(y)
        bawah=(((statistic._variation(x)**2)/len(x))+((statistic._variation(x)**2)/len(x)))
        result=atas/pow((bawah),0.5)
        return result
    def std_dev(x):
        std_x=sum([pow((i-statistic._mean(x)),2) for i in x])
        le_pol=len(x)-1
        result=std_x/le_pol
        return pow(result,0.5)
    def reges(x,y):
        "https://datascience.stackexchange.com/questions/80308/dose-finding-slope-intercept-using-the-formula-of-m-b-gives-best-fit-line-always"
        xy=sum(np.array(x)*np.array(y))
        sum_x=sum(np.array(x))
        sum_y=sum(np.array(y))
        x2=np.array(x)**2
        n=len(x)
        m=((n*xy)-(sum_x*sum_y)/((n*x2)-(sum_x**2)))
        b=(sum_y-m*sum_x)/len(x)
        data_reg=pd.DataFrame(
            {
                "m":m,
                "b":b
            }
        )
        m_pilih=statistic._mode(data_reg.m)
        b_pilih=statistic._mode(data_reg.b)

        result=[]
        for i in x:
            formula=i*m_pilih+b_pilih
        result.append(formula)
        return result
        
        # tambahan
        

        return b
        # return f"rumusnya jadi Y={m}x+{b}"

    
        

