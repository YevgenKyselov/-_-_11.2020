# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.
my_list = ['abc', 'abc', 'abc']
res_list = []
for index, value in enumerate(my_list):
    if not index % 2:
        new_str = my_list[index]
        res_list.append(new_str[::-1])
    else:
        res_list.append(my_list[index])
print(res_list)
################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ['abc', 'def', 'aZZ']
a_list = []
for index, value in enumerate(my_list):
    temp_str = str(my_list[index])
    if temp_str[0] == 'a':
        a_list.append(temp_str)
print(a_list)
################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ['zbc', 'defa', 'AZZa']
a_list2 = []
for index, value in enumerate(my_list):
    temp_str = str(my_list[index])
    if temp_str.find('a') > 0:
        a_list2.append(temp_str)
print(a_list2)
###############################
# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.
my_list = ['zbc', 'defa', 'AZZa', 1, 6456]
str_list = []
for index, value in enumerate(my_list):
    temp_str = str(my_list[index])
    if not temp_str.isdigit():
        str_list.append(temp_str)
print(str_list)
###############################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
my_str = 'abbbbbb'
uniq_list = []
for symbol in my_str:
    if not my_str.count(symbol) > 1:
        uniq_list.append(symbol)
print(uniq_list)
################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
str_1 = "aabcdef55"
str_2 = "ajklmno55"
my_values_1,  my_values_2 = set(str_1), set(str_2)
my_list = list(my_values_1.intersection(my_values_2))
print(my_list)
################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
str_1 = "abbcdde"
str_2 = "eddcbb"
my_list = []
my_list_2 = []
for symbol in str_1:
    if not str_1.count(symbol) > 1:
        my_list.append(symbol)
for symbol in str_2:
    if not str_2.count(symbol) > 1:
        my_list_2.append(symbol)
my_values_1, my_values_2 = set(my_list), set(my_list_2)
values_res = my_values_1.intersection(my_values_2)
list_res = list(values_res)
print(list_res)
