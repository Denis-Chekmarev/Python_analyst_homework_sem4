"""
Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.

Пример: при N = 12 -> [2, 3]

"""

from functions import get_number


def get_simple_mult(number: int) -> list:
    result = []
    while number % 2 == 0:
        result.append(2)
        number /= 2
    for i in range(3 , int(number**0.5+1), 2):
        while number % i == 0:
            result.append(i)
            number /= i
    if number > 2:
        result.append(int(number))
    return list(set(result))


N = get_number('Input the number -> ')
while N < 2:
    N = get_number('Input is incorrect. Please input number bigger than 1 -> ')
simple_mult = get_simple_mult(N)
print(simple_mult)