

def co_mean(lst):
    return (sum(lst)/len(lst))

def co_var(lst):
    mn=co_mean(lst)
    su=0
    for i in lst:
        su+=((i-mn)**2)
    return (su/(len(lst)-1))

def co_std(lst):
    mn=co_mean(lst)
    su=0
    for i in lst:
        su+=((i-mn)**2)
    return (su/(len(lst)))

def co_se(lst):
    st=co_std(lst)
    return (st/(len(lst)**(1/2)))

def co_z(dp,lst):
    st=co_std(lst)
    mn=co_mean(lst)
    return ((dp-mn)/st)
    
    
