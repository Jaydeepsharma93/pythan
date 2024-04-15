def Reverse(arr): 
   new_lst = arr[::-1]
   return new_lst
 
arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter Position",i,":")
    ele = int(input())
    arr.append(ele)
print(Reverse(arr))