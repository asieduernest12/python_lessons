# todo writing 3 programs, 
# program1 outputs "name" and hello
# program2 outputs a+b
# program3 outputs even numbers up to x, where x >=2

# greet function outputs a greeting with the name submitted as its input
def greet(name):
    print("Good evening " + name)
# adder function outputs sum of two inputs 
def adder(a,b):
    result = str(a + b)
    print("result is => " + result )

# area function prints the multiplicated results of two parameters
def areaofrec(length,breadth):
    print(str(length * breadth))


# main function is the default function called when a python file is executed
def main():
    greet("Mensa") # calling greet function with "Mensa" the value for name var
    greet("Dan") # Dan will be value for name var
    adder(19,1) # calling adder with two inputs to added and printed
    areaofrec(20,3) 
    areaofrec(22,5)

if __name__ == "__main__":
    main()