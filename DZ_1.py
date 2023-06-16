# Найдите сумму цифр трехзначного числа.
#  Число 123

a = int(input("Введите число: "))

summ = 0

while a > 0:
    x  = a % 10
    summ = summ + x
    a = a // 10
else:
    print("Задание завершено")
    print(summ)