def inversionCount(a,n):
    # Your Code Here
    b = a.copy()
    b.sort(reverse = True)
    sum = 0
    for i in range(0,n):
        value = a[i]
        print(b.index(value))
        sum = sum + abs(b.index(value) - (i+1))
    if sum >0:
        return int(sum/2)
    else :
        return 0


a = [2, 4, 1, 3, 5]
n = len(a[:4])
ind = a.index(5)
print(ind)
print(n)
# result = inversionCount(a,n)
# print(result)