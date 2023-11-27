print("Enter your choice of operation:-\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division")
x=True
while x:
    a=int(input("Enter a number: "))
    b=int(input("Enter the second number: "))   
    c=int(input("Please enter your choice of operation: "))
    if(c==1):
        print("The answer is",a+b)
    elif(c==2):
        print("The answer is",a-b)
    elif(c==3):
        print("The answer is",a*b)
    elif(c==4):
        print("The answer is",a/b)
    else:
        print("Invalid choice!")
    d=input("Do you want to continue? (y/n) :    ").lower()
    if not(d=="y"):
        x=False
print("Thank You!")
