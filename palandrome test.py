def palandr():
    qwestion = input('Введите слово: ')
    if qwestion.lower() == qwestion.lower()[::-1]:
        print('Эта строка является паландромом.\n')
    else:
        print('Эта строка не является паландрономом.\n')
    return palandr()
print('Привет! Эта программа проверяет слово на паландром.')
palandr()

