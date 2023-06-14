def avg(N):
    sum = 0
    for i in N:
        sum = sum + i
    avg = sum / len(N)
    return avg
print(avg([1,2,3]))
