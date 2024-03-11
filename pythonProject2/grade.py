n1=int(input("enter the marks you got :"))
def mark(n1):
    if (n1>=90):
        return ("grade A")
    elif (n1>=80):
        return (" grade B")
    elif (n1>=70):
        return (" grade C")
    else:
        return ("grade D")

res=mark(n1)
print(res)