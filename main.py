print("fjk")
print(2 + 6)

print("n")
    #print(2+6)

if 1 < 2:
    print('Привет')
else:
    print('пока')

#стандарт PEP8
# регистрозависимость
# Print('hello') - неправильно

#print('hello world') - строчный комментарий

''' False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield'''

name = 'zxc'
print(type(name))
#два типа наименования переменных

#camel case
username = 'zxc'

#understore notation
user_name = 'zxc'

#две переменные разные
age = 23
Age = 23
age = 34
print(age)

''' False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield'''
#Числовые типы данных
'''
int- Целые числа x=5
float - вещественный тип данных(число с плавающей точкой) y=5.6

'''

#Текстовые типы данных
'''
str - Строка, состоящие из символов, заключенных в одинарные или двойные кавычки
name="Фил"
'''
#Логические типы данных
'''
bool - Логические значения (True-истина,False-ложь)

is_activate=True
'''

#Cписки и коллекции

#None
'''
NoneType- особый тип данных, который представляет отсутствие значения 
z=None
'''

a = 5
b = 5.6
c = 'zxc'
d = True
r = None
c1 = "zxc"
print(a, b, c, d, r, c1)

#print(значение, end - конечный символ)

# print('привет мир', end=' ')
# print('привет мир', end=' и пока')

name = input()
print(name)

age = int(input('Введите возраст: '))
print(age)

#2-10
a = 0b11
b = 0b1011
print(a, b)

#явное преобразование
x = 10
y = str(x)
z = float(x)
print(type(y))
print(type(z))

#автоматическое преобразование данных

y = 6
x = y + 8.9
print(type(x))

complexnumber = 2 +3j
print(complexnumber)

text = 'Сообщение:\n\"Привет друзья!\"'
print(text)

#print(значение, end=конечные символы)

print('hello', end='\n')
print('hello', end='my friend')

print(5 + 5)
print(10 - 5)
print(3 * 4)
print(8 / 2)
print(25 // 4)
print(50 % 2)
print(2 ** 2)

# ** - справо налево
# * // / % слева направо
# + - слева направо

#арифм с присвоением

s = 5
print(s)
s += 5
print(s)
s -= 5
print(s)
s *= 5
print(s)
s /= 5
print(s)
s //= 5
print(s)
s %= 5
print(s)
s **= 5
print(s)

#округление чисел

num_1 = 2.0001
num_2 = 5
num_3 = num_1 + num_2
print(num_3)
print(round(num_3))

#Операторы сравнения
res=(5>3)
print(res)
res=(5<3)
print(res)
res=(5==3)
print(res)
res=(5!=3)
print(res)
res=(5<=3)
print(res)
res=(5>=3)
print(res)