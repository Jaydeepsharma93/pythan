def findPeri(a, b):
    p = 2*(a+b)
    return p

l = float(input("Enter Length of Rectangle : "))
b = float(input("Enter Breadth of Rectangle : "))

res = findPeri(l, b)
print("\nPerimeter = {:.2f}".format(res))