def fun(l1,l2):
    for item in l1:
        if item in l2:
            return True
    return False   
print(fun([1,2,3,4],[4,5,6,7,8]))
print(fun([1,2,3,4],[5,6,7,8]))