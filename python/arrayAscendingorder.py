arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter Position",i,":")
    ele = int(input())
    arr.append(ele)
 
arr.sort()
print("array in ascending order :",arr)