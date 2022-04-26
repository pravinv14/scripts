"""
python program to 
 print FizzBuzz, if integer is multiple of both 3 and 5
 print Fizz, if integer is multiple of 3 but not 5
 print Buzz, if integer is multiple of 5 but not 3
 print integer, if integer is not multiple of both 3 and 5
"""

def fizz_buzz(n):
    string = ''
    if n % 3==0: string +='Fizz' 
    if n % 5==0: string +='Buzz'
    return string if string else n

if __name__ == "__main__":
    n = int(input().strip())
    for n in range(1, n+1):
        print(fizz_buzz(n))
