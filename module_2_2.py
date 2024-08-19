first = int(input('Введите число от 1 до 10: '))
second = int(input('Введите число от 1 до 10: '))
third = int(input('Введите число от 1 до 10: '))
if first == second == third:
    print(3)
elif first == second != third or first == third != second or first != second == third:
    print(2)
else:
    print(0)