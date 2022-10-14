print('Введите число чтобы вычислить его факториал')
a=int(input())
factorial=1
while a > 1:
    factorial*=a
    a-=1
print('Выведен факториал числа')
print(factorial)