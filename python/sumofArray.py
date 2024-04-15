arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter Position",i,":")
    ele = int(input())
    arr.append(ele) 
print ("sum of elements in an array is :", sum(arr))