# Напишіть функцію commonStr що задовільняє наступній умові:



# Дано дві строчки, поверніть нову строчку 
# яка буде складатись виключно зі спільних символів перерадних строк.
# Якщо немає спільних символів - поверніть пусту строчку. 
# Ви можете повернути відповідь у будь-якому порядку.
# Символи не повині дублюватись у відповіді.

# Приклад 1
# commonStr('loli', 'luck') -> 'l'

# Приклад 1
# commonStr('good day', 'good morning') -> 'god'


str1 = input()
str2 = input()
def commonStr():
    comparison = list(set(str1) & set(str2))
    a = ''.join(comparison)
    b = a.split()
    c = ''.join(b)
    print(c)
commonStr()