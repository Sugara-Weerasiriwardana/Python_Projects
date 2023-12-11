
number = int(input("enter a number : "))
prime=True
for num in range(2,number):
    if number % num ==0:
        prime = False


if prime:
    print("Prime")    
else:
    print("Not Prime")    