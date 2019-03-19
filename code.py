# todo writing 3 programs, 
# program1 outputs "name" and hello
# program2 outputs a+b
# program3 outputs even numbers up to x, where x >=2

def greet(name):
    print("Good evening " + name)

def adder(a,b):
    result = str(a + b)
    print("result is => " + result )

def areaofrec(length,breadth):
    print(str(length * breadth))


# main function is the default function called when a python file is executed
def main():
    greet("Mensa")
    greet("Dan")
    adder(19,1)
    areaofrec(20,3)
    areaofrec(22,5)

if __name__ == "__main__":
    main()