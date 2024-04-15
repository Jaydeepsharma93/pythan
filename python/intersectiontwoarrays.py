from functools import reduce
arr = []
arr2 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("arr1 Position",i,":")
    ele = int(input())
    arr.append(ele)

for i in range(0, n):
    print("arr2 Position",i,":")
    ele = int(input())
    arr2.append(ele)

intersection = reduce(lambda acc, x: acc + [x] if x in arr2 and x not in acc else acc, arr, [])
 
print("the intersection of two arrays : ",intersection)