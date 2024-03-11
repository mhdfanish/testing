n=int(input("enter your age:"))
def vote(n):
    if (n<=18):
        print("you are not eligible for vote")
    else:
        print("you are eligible for voting")

vote(n)
