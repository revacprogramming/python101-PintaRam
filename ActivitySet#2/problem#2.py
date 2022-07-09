
def add(a, b):
    return a+b;


def output(a, b, sum):
    print(f" sum of {a} + {b} is {sum}");


def main():
    a = float(input("enter the first number : "));
    b = float(input("enter the second number : ")); 
    sum = add(a, b);

    output(a, b, sum)

name = "__main__";
if __name__ == '__main__':
    main()
