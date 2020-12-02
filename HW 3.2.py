# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
my_value = int(input())
new_value = my_value/2 if my_value < 100 else my_value*-1
print(new_value)
################################
# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0
my_value = int(input())
new_value = 1 if my_value < 100 else 0
print(new_value)
################################
# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False
my_value = int(input())
new_value = True if my_value < 100 else False
print(new_value)
################################
# 4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
my_str =  "Test string 123 QWE"
for symbol in my_str:
    my_new_str = my_str.upper()
print(my_new_str)
################################
# 5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
my_str =  "Test string 123 QWE"
for symbol in my_str:
    my_new_str = my_str.lower()
print(my_new_str)
################################
# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример:
# было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
my_str =  "Test string 123 QWE"
my_new_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_new_str)
################################
# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
my_str =  "Test string 123 QWE"
my_new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_new_str)
################################
# 8) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые являются буквой или цифрой.
my_str =  "Test string 123 QWE"
for symbol in my_str:
    if symbol.isalnum():
        print(symbol)
################################
# 9) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.
my_str =  "Test string #123 QWE"
for symbol in my_str:
    if not symbol.isalnum():
        print(symbol)
################################
# 10) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой ти не пробел.
my_str = "Test _string#123 QWE"
for symbol in my_str:
    if not symbol.isalnum() or not " ":
        print(symbol)
