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
    def median_val(data:list):
        # first must be sorted from smallest to biggest
        """
        for paper/journal reference:
            https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/median/
        """
        data.sort()
        dummy=data
        n=len(data)

        if n%2 !=0:
            # odd lenght data
            index=int((n+1)/2)
            result=dummy[index-1]
        else:
            index=[int((n/2)+int((n/2)+1))]
            result=dummy[index[0]:index[1]+1]
        return result
    def _mode(data:list):
        # first data be sort from smallest to biggest
        # dummy data variabel
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


