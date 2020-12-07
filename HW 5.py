# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# number = 1000300
# my_str = str(number)
# value = my_str.count('0')
# print(value)
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
# number = 10060300
# my_str = str(number)
# new_str = str(int(my_str[::-1]))
# value = len(my_str)-len(new_str)
# print(value)
# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 15, 20, 25]
# my_result = []
##########################
# for symbol in my_list_1:
#     if symbol % 2 == 0:
#         my_result.append(symbol)
##########################
# for symbol in my_list_2:
#     if symbol % 2 != 0:
#         my_result.append(symbol)
# print(my_result)
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
# my_list = [1, 2, 3, 4]
# new_list = my_list.copy()
# del new_list[0]
# new_list.append(my_list[0])
# print(new_list)
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
# my_list = [1, 2, 3, 4] # почему PyCharm "ругается" в этой строке?
# my_list.append(my_list[0])
# my_list.pop(0)
# print(my_list)
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.
# my_str = "43 больше чем 34 но меньше чем 56"
# my_list = my_str.split(" ")
# sum = 0
#########################
# for symbol in my_list:
#     try:
#         value = int(symbol)
#         sum += value
#     except:
#         ValueError
# print(sum)
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
my_str = 'ab2323232'
my_list = []
i = 0
j = 1
if len(my_str) % 2 == 0:
    for symbol in my_str:
        try:
            new_str = my_str[i] + my_str[j]
            i += 2
            j += 2
            my_list.append(new_str)
        except: IndexError
else:
    my_str += '_'
    for symbol in my_str:
       try:
            new_str = my_str[i] + my_str[j]
            i += 2
            j += 2
            my_list.append(new_str)
       except: IndexError
print(my_list)
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
index_1 = my_str.find(l_limit)
index_2 = my_str.rfind(r_limit)
sub_str = my_str[index_1+1:index_2]
print(sub_str)
