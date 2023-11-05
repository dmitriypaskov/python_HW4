#Програма має виконувати прості математичні дії (+, -, *, /).
#Користувачеві пропонується почерзі ввести числа та дію над цими числами,
#а програма, виходячи з дії, обчислює та друкує результат.
#Зробити перевірку на те, що при діленні дільник не дорівнює 0!
#Приклад:
#Please enter first number: 3
#Please enter second number: 5
#Please enter action: +
#Your result is 8
#Приклад с діленням на нуль:
#Please enter first number: 10
#Please enter second number: 0
#Please enter action: /
#You can't divide by 0'
a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))
act = input('Please enter action: ')
if act == '+':
    print("You result ", a + b)
if act == '-':
    print("You result ", a - b)
if act == '*':
    print("You result ", a * b)
if act == '/' and b != 0:
    print("You result ", a / b)
elif act == '/' and b == 0:
    print("You can't divide by 0")

