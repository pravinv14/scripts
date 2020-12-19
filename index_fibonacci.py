#  To run this use python index_fibonacci.py
#  Index of a Fibonacci number
#  This code will be updated with try except block to handle errors/wrong input

try:
    print(50*'#')
    print("This script does not evaluate if Fibonacci or not...")
    inp = int(input("Enter a fibonacci number and get its index! : "))
    print(50*'#')
    
    def findIndex(inp):
        if (inp <= 2):
            return inp
        a = 0
        b = 1
        c = 1
        result = 1
        while (c < inp):
            c = a + b
            result = result + 1
            a = b
            b = c
        return result
    
    out = findIndex(inp)
    print(f'At index :',out)
except:
    print("Please input a Whole number!")
