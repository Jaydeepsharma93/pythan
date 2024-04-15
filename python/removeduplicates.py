arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("arr1 Position",i,":")
    ele = int(input())
    arr.append(ele)
print ("The original array is : "
        + str(arr))

arr = list(set(arr))
print ("after remove duplicates from an array : "
        + str(arr))