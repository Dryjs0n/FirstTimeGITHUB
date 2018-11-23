def fibonacci(n):
    i=2
    a=[]
    if(n==0):
        a.append(0)
        return a
    if(n==1):
        a.append(0)
        a.append(1)
        return a
    if(n>1):
        a.append(0)
        a.append(1)
        for i in range(i, n):
            a.append(a[i-2]+a[i-1])
        return a
