def binarysubstring(str,n):
    count0 = 0
    count1 = 0
    count = 0
    for i in range(0,n):
        if str[i] == '0':
            count0 += 1
        else :
            count1 += 1
        if count0 == count1:
            count += 1

    if count > 0:
        return count
    else:
        return -1

str = "0100110101"
n = len(str)
print(binarysubstring(str, n))


