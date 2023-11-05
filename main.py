#Програма має виконувати прості математичні дії (+, -, *, /).
#Користувачеві пропонується почерзі ввести числа та дію над цими числами,
#а програма, виходячи з дії, обчислює та друкує результат.
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

