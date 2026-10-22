# 1
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = set(numbers)
print("Множество:", unique_numbers)
print("Количество элементов:", len(unique_numbers))

# 2
numbers = {10, 20, 30}
numbers.add(40)
numbers.remove(20)
print("Результат:", numbers)

# 3 
a = {1, 2, 3}
b = {3, 4, 5}
print("Объединение:", a | b)

# 4
a = {1, 2, 3}
b = {3, 4, 5}
print("Пересечение:", a & b)

# 5
a = {1, 2, 3}
b = {3, 4, 5}
print("Есть только в первом:", a - b)
print("Есть только во втором:", b - a)

# 6
a = {1, 2, 3}
b = {3, 4, 5}
print("Симметрическая разность:", a ^ b)

# 7
numbers = {2, 4, 6, 8}
x = 6
print("Число есть в множестве:", x in numbers)

# 8
a = {1, 2}
b = {1, 2, 3, 4}
print("Первое является подмножеством второго:", a <= b)

# 9
text = "программирование"
characters = set(text)
print("Различные символы:", characters)
print("Количество:", len(characters))

# 10
first = [5, 1, 2, 2, 3, 5]
second = [3, 3, 4, 5, 2]
common = sorted(set(first) & set(second))   
print("Общие элементы:", common)
