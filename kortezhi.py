# 1
numbers = (10, 20, 30, 40, 50)
print("Первый:", numbers[0])
print("Последний:", numbers[-1])
print("Средний:", numbers[len(numbers) // 2])

# 2
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print("Первые два:", numbers[:2])
print("Последние два:", numbers[-2:])
print("Обратный порядок:", numbers[::-1])

# 3
numbers = (7, 2, 9, 4, 1)
print("Длина:", len(numbers))
print("Сумма:", sum(numbers))
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))

# 4
numbers = (1, 3, 5, 3, 7, 3)
x = 3
print("Число есть в кортеже:", x in numbers)
print("Количество вхождений:", numbers.count(x))
if x in numbers:
    print("Индекс первого вхождения:", numbers.index(x))
else:
    print("Первого вхождения нет")

# 5
first = (1, 2, 3)
second = (4, 5, 6)
print("Объединённый кортеж:", first + second)

# 6
single = (42,)
print("Тип:", type(single))

# 7
person = ("Анна", 18, "Москва")
name, age, city = person
print("Имя:", name)
print("Возраст:", age)
print("Город:", city)

# 8
a = 10
b = 20
print("До обмена:", a, b)
a, b = b, a
print("После обмена:", a, b)

# 9
original = (10, 20, 30, 40)
updated = original[:1] + (99,) + original[2:]
print("Новый кортеж:", updated)

# 10
numbers = (5, 2, 3, 2, 1, 5, 3)
result = tuple(sorted(set(numbers)))
print("Без повторов по возрастанию:", result)
