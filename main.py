a = int(input('Który wyraz ciągu? '))
creds = ' fibonacci \n Grzegorz Zaręba \n Grupa 1.5 - piątek 14:00'
def fib(n):
    n -= 1
    a = 0
    b = 1
    d = a + b
    i = 3
    if n == 0:
        d = 0
    elif n == 1:
        d = 1
    elif n > 1:
        while i <= n:
            a = b
            b = d
            d = a + b
            i += 1
    print(d)
    print(creds)

fib(a)