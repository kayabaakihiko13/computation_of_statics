def factorial(n):
    if n<0:
        raise Exception("sorry")
    if n==0:
        return 1
        
    else:
        return n* factorial(n-1)
def exponatial_eval(x):
    
    e=2.718281 # eular number
    if (type(x)!=list):
        return e**x
    else:
        memo=[]
        for i in x:
            i=i**e
            memo.append(i)
        return memo