name=input("enter students name:")
lastname=input("enter students lastname:")
exam1score=float(input("enter students exam 1 score"))
exam2score=float(input("enter students exam 2 score"))
exam3score=float(input("enter students exam 3 score"))
mean=(exam1score+exam2score+exam3score)/3
if mean>=17:
    print(name,lastname,"result is great")
elif mean>=12 and mean<17:
    print(name,lastname,"result is normal")
else:
    print(name,lastname,"result is fail")

