def printoccurence(arr,x):
    start,end = 0, 0
    for i in range(len(arr)):
        if arr[i] == x:
            if start == 0:
                start = i
            end = i
    return start,end

def printfirstoccur(arr,i,j,x,n):
    if j>=i:
        mid = i+(j-i) // 2
        if ((mid==0 or x>arr[mid-1]) and arr[mid] == x):
            return mid
        if arr[mid] < x:
            return printfirstoccur(arr, mid + 1, j, x,n)
        else:
            return printfirstoccur(arr, i, mid - 1, x,n)
    return -1

def printlastoccur(arr,i,j,x,n):
    if j>=i:
        mid = i+(j-i) // 2
        if ((mid ==n-1 or x<arr[mid+1]) and arr[mid] == x):
            return mid
        if arr[mid] < x:
            return printlastoccur(arr,mid + 1,j,x,n)
        else:
            return printlastoccur(arr,i,mid - 1,x,n)
    return -1

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
print(printfirstoccur(arr,0,n-1,x,n))
print(printlastoccur(arr,0,n-1,x,n))


