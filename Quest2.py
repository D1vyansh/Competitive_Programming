# Maximum and minimum of an array using minimum number of comparisons
# Time complexity - O()
#----------------------------------------------------
class struct:
    def __init__(self):
        self.min = 0
        self.max = 0

def minmaxfunc(arr):
    minmax = struct()
    if len(arr) ==1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else :
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, len(arr)):
        if(arr[i]>minmax.max):
            minmax.max = arr[i]
        elif(arr[i]<minmax.min):
            minmax.min = arr[i]

    return minmax

a= [100, 11,1,20,3000,400]
result = minmaxfunc(a)
print(result.min, result.max)






