print('1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);')
def prime(n):
    i = 2
    while n > i:
        if n % i == 0:
            return (n,'непростое число')
        i += 1
        if i == n:
            return (n,'простое число')
print(prime(51))
print(prime(17))

print('2) функция выводит список всех делителей числа:', 256)
def denominator(n):
    result = []
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result
print(denominator(256))

print('3) выводит самый большой простой делитель числа')
from functools import reduce
def max_denominator(n):
    max_number = denominator(n)
    max_number = reduce(lambda a,b: a if a>b else b, max_number)
    return(max_number)
print(max_denominator(256))