def med(data:list):
    data.sort()
    dummy_data=data
    n=len(data)
    if n%2==0: #for genap
        indeks=[int(n/2),int((n/2)+1)]
        result=sum(dummy_data[indeks[0]-1:indeks[1]])/2
        
    else:
        indeks=int((n+1)/2)
        result=sum(dummy_data[indeks[0]-1:indeks[1]])/2
    return result
def varian(data:list):
    dummy_data=0#dummy data
    n=len(data)
    for i in data:
        dummy_data+=pow((i-med(data)),2)
    result=dummy_data/(n-1)
    return result

def rata_rata(data:list):
    dummy_data=0
    count=0
    for a in data:
        dummy_data+=a
        count+=1
    return(f"{dummy_data/count:.5f}")