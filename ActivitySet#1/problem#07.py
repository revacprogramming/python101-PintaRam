"""Write a program that repeatedly prompts a user for integer numbers until the user enters don'. Once done is entere print out the largest and smallest of the numbers."""
largest = None
smallest = None
num1 = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num) 
        num1.append(num)
        if largest is None or largest < num: 
            largest = num
        if smallest is None or smallest > num: 
            smallest = num
    except:
        print ("Invalid input")
        continue
print ("Maximum is",largest)
print ("Minimum is",smallest)