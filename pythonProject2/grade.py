n1=int(input("enter the marks you got :"))
def mark(n1):
    if (n1>=90):
        print("you got A grade")
    elif (n1>=80):
        print("you got B grade")
    elif (n1>=70):
        print("you got C grade")
    else:
        print("------------better luck next time--------------")

mark(n1)