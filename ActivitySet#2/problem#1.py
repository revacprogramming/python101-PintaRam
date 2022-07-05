def add(a, b):
    return a+b

def main():
    a = float(input("enter the first number : "));
    b = float(input("enter the second number : ")); 
    c = add(a, b);
    print(f" sum of {a} + {b} = {c}");

main();