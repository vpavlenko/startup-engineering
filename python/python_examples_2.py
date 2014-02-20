# словарь - соответствие из ключей в значения
# это как список, только индексы могут быть не только числами
dictionary = {}
dictionary['half-blood'] = 'полукровка'
dictionary['cauldron'] = 'котёл'
dictionary['potion'] = 'зелье'
print(dictionary['cauldron'])
print('potion' in dictionary)
print('зелье' in dictionary)
print('quidditch' in dictionary)

try:
    print(dictionary['quidditch'])
except KeyError as e:
    print('Мы поймали исключение:', e)

print(dictionary.get('half-blood', 'неизвестно'))
print(dictionary.get('quidditch', 'неизвестно'))

# всё нумеруется с нуля. отрицательные индексы идут
# из конца в начало.
s = 'abcdefghi'
print(s[0], s[1], s[-1], s[-2])

# типов переменных нет. есть объекты и ссылки на них
s = [5, 10, 'smth', {'A': 'a'}]
print(s[0], s[1], s[-1], s[-2])

# есть срезы
a = list(range(11, -1, -1))
b = a[3:6]
c = [2:]
d = [2::2]
e = a[6:3:-1]
f = a[6::-1]
g = a[::-1]

# всё то же самое работает над строками
a = s
b = a[3:6]
c = [2:]
d = [2::2]
e = a[6:3:-1]
f = a[6::-1]
g = a[::-1]

# создание двумерного списка
a = [0] * 3
a[0] = 1
a[1] = 'a' * 5

# создание двумерного списка
a = [[0] * 3] * 2
a[0][0] = 'приплыли'

# правильный способ
a = [[0] * 3 for i in range(2)]

# кстати о range: тут так делают цикл for
s = ''
for i in range(5, 8):
    s += str(i)
