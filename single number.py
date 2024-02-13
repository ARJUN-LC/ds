def singlenum(num):
    n=[]
    for i in num:
        if i not in n:
            n.append(i)
        else:
            n.remove(i)

    print(n)

m=[2,2,1]
print(singlenum(m))

