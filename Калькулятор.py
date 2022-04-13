# Калькулятор v2

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.CYAN)

what = input("Выбирите действие (+, -, *, /)")

a = float(input("Первое число: "))
b = float(input("Второе число: "))

if what == "+":
	c = a + b
	print("=" + str(c))
elif what == "-":
	c = a - b
	print("=" + str(c))
elif what == "*":
	c = a * b
	print("=" + str(c))
elif what == "/":
	c = a / b
	print("=" + str(c))
else:
	print("Выбрано неверное действие")

input()
