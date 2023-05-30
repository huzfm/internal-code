def sum(str):
    add=0
    for i in str:
        if i.isdigit()==True:
            z=int(i)
            add = add + z
    return add
def avg(str):
    add=0
    count=0
    for x in str:
        if x.isdigit():
            add += int(x)
            count += 1
    return add/count
print(sum('1233asdad1e1'))
print(avg('123242098240idwdfe244'))