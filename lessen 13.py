try:
    x = int (input())
except ValueError:
    print("Вы ввели не число")
    x = 0
print(x)
try:
    y = int (input())
except ValueError:
    print("Вы ввели не число")
    y = 0
else:
    print("Всё верно")
finally:
    print("Выполнится 100%")

print(x)
x = int(input())
y = int(input())
try:
   res = x/y
except ZeroDivisionError:
   print("Вы ввели 0")
res = 0
print(res)

