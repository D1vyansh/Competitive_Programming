def search2D(needle, strr,i,j,n,m):
    dir = [[-1, 0], [1, 0],[0, 1],[0, -1]]
    if strr[i][j] != needle[0]:
        return False
    for x,y in dir:
        flag = True
        rd, cd = i + x, j + y
        for k in range(1,len(needle)):
            if 0 <=rd <n and 0 <=cd< m and strr[rd][cd] == needle[k]:
                rd += x
                cd += y
            else:
                flag = False
                break
        if flag:
            return True
    return False

def searchString(needle, strr,n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if search2D(needle, strr,i,j,n,m):
                print("pattern found at " +
                           str(i) + ', ' + str(j))
                count += 1
    return count


needle = "MAGIC"
inputt = ["BBABBM", "CBMBBA", "IBABBG",
          "GOZBBI", "ABBBBC", "MCIGAM"]

# strr = [0] * len(inputt)
# for i in range(len(inputt)):
#     strr[i] = list(inputt[i])
print("count: ", searchString(needle,inputt,
                              len(inputt), len(inputt[0])))




