# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перевірить певне число на те чи воно парне або непарне.

# Функція приймає на вхід будь яке число і виводить в консоль строку типу 'Число Х є парним'.
# Наприклад:
#   oddOrEven(1) - > 'Число Х є непарним'
#   oddOrEven(20) - > 'Число Х є парним'
# Можна додавати свої тести за прикладом. Потрібно врахувати обробку можливих помилок.


num = int(input())

def oddOrEven():
    if num % 2 == 0:
        print('Число', num, 'є парним')
    else:
        print('Число', num, 'непарним')
oddOrEven()
