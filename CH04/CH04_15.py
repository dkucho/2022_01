a=input("Enter an interger: ")
while not a.isnumeric():
    print("Enter numbers.")
    a=input("Enter an integer: ")
a=int(a)
print(a, type(a))
