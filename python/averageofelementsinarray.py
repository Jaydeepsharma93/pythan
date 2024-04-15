def Average(arr): 
    return sum(arr) / len(arr) 

arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter Position",i,":")
    ele = int(input())
    arr.append(ele)
average = Average(arr) 
print("Average of the Array =", round(average, 2))