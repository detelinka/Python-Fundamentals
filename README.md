Data Types and Variables / Типове данни ￼

```python
# Основни типове
int_num = 10             # int
float_num = 10.2         # float
a_str = "Hello"          # str
is_true = True           # bool

# Проверка на типа
print(type("123"))       # <class 'str'>
print(type(123))         # <class 'int'>
print(isinstance("123", str))  # True

# Преобразуване на типове
x = int("5")             # 5
y = float("3.14")        # 3.14
s = str(3.5)             # "3.5"

# Булеви изрази и сравнения
a == b       # равно
a != b       # различно
a < b        # по-малко
a <= b       # по-малко или равно
a > b        # по-голямо
a >= b       # по-голямо или равно

```

```python
# Стринг – последователност от символи
name = "George"
print(name[0])       # 'G'
print(len(name))     # дължина

# f-string (интерполация)
name = "Rick"
age = 18
print(f"{name} = {age}")   # Rick = 18

```

```python
# Числа – практични задачи
# Meters to Kilometers
meters = int(input())
kilometers = meters / 1000
print(f"{kilometers:.2f}")

# Pounds to Dollars (1 GBP = 1.31 USD)
pounds = int(input())
dollars = pounds * 1.31
print(f"{dollars:.3f}")

```

Basic Syntax, Conditionals and Loops ￼

```python
# Променливи
age = 25      # name: age, value: 25

# Условни конструкции
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("b is not greater than a")

```

```python
# Логически оператори
if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one is True")

if not a > c:
    print("Condition is False")

# Проверка дали число е в интервал
a = int(input())
if 1 <= a <= 10:
    print("a is in the range 1 and 10")

```

```python
# for с range()
for x in range(3):
    print(x)    # 0, 1, 2

# Обхождане на стринг отзад напред
word = input()
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

```

```python
# break / continue / for-else
for x in range(3):
    if x == 1:
        break
    print(x)        # 0

for x in range(3):
    if x == 1:
        continue
    print(x)        # 0 2

for x in range(3):
    if x == 3:
        break
else:
    print("Finish") # ще се принтира

```

```python
# while цикъл
i = 1
while i < 6:
    print(i)
    i += 1

# Number Between 1 and 100
number = float(input())
while not (1 <= number <= 100):
    number = float(input())
print(f"The number {number} is between 1 and 100")

```

Lists Basics / Листове – основи ￼

```python
# Дефиниране
nums = [1, 2, 3]
empty_list = []
mixed = [7, "Peter", 9.99]

# Създаване от стринг
some_text = "a b c d"
my_list = some_text.split(" ")       # ['a', 'b', 'c', 'd']

# join обратно към стринг
print("-".join(["a", "b", "c"]))     # "a-b-c"

```

```python
# Достъп по индекс (+ и -)
list_of_numbers = [1, 5, 7]
print(list_of_numbers[0])   # 1

my_pets = ["cat", "dog", "parrot"]
print(my_pets[-1])          # parrot

```

```python
# Добавяне / махане
my_list = [1, 2, 3]
my_list.append(4)                   # [1, 2, 3, 4]
my_list.extend([5, 6])              # [1, 2, 3, 4, 5, 6]
my_list.insert(1, 100)              # [1, 100, 2, 3, 4, 5, 6]

my_list.remove(100)                 # по стойност
number = my_list.pop(0)             # по индекс, връща елемента
my_list.clear()                     # []

```

```python
# Итерация през лист
my_list = ["dog", "cat", "fish"]

for element in my_list:
    print(element, end=" ")

for i in range(len(my_list)):
    print(my_list[i], end=" ")

# while
i = 0
while i < len(my_list):
    print(my_list[i], end=" ")
    i += 1

```

```python
# Примери от задачи
# Courses
n = int(input())
courses = []
for _ in range(n):
    courses.append(input())
print(courses)

# List Statistics
n = int(input())
positives = []
negatives = []
for _ in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

```

Lists Advanced / Листове – напреднали ￼

```python
# List comprehensions – шаблон
x = [num for num in range(5)]                # [0, 1, 2, 3, 4]
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]               # [1, 4, 9, 16]

# с if / if-else
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]      # [2, 4, 6]
filtered = [True if x % 2 == 0 else False for x in nums]

```

```python
# No Vowels
text = input()
vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
no_vowels = "".join([ch for ch in text if ch not in vowels])
print(no_vowels)

```

```python
# Допълнителни методи
my_list = [1, 2, 3, 2, 2]
my_list.count(2)          # 3
pos = my_list.index(2)    # 1
my_list.reverse()         # [2, 2, 3, 2, 1]

# Размяна на елементи
nums = [1, 2, 3]
nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]
# [3, 1, 2]

# Слепване на листове
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
final_list = nums1 + nums2           # [1, 2, 3, 4, 5, 6]

# Уникални елементи
numbers = [1, 2, 2, 3, 1, 4, 5, 4]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]

```

```python
# sorted, map, filter, reduce
from functools import reduce

numbers_list = [6, 2, 1, 4, 3, 5]
sorted_asc = sorted(numbers_list)                         # [1,2,3,4,5,6]
sorted_desc = sorted(numbers_list, key=lambda x: -x)      # [6,5,4,3,2,1]

strings_list = ["1", "2", "3"]
ints = list(map(int, strings_list))                       # [1,2,3]

doubled = list(map(lambda x: x * 2, ints))                # [2,4,6]
even = list(filter(lambda x: x % 2 == 0, ints))           # [2]

total = reduce(lambda a, b: a + b, ints)                  # сума
mx = reduce(lambda a, b: a if a > b else b, ints)         # макс

```

Functions / Функции ￼

```python
# Декларация и извикване
def print_text(text):
    print(text)

print_text("Hello")

# без параметри
def multiply_numbers():
    result = 5 * 5
    print(result)

multiply_numbers()

```

```python
# return
def give_me_five():
    return 5

print(give_me_five())   # директно
num = give_me_five()    # в променлива
print(num)

```

```python
# параметри, аргументи, default, keyword
def person(first_name="George", last_name="Brown"):
    print(first_name, last_name)

person("Peter")                 # Peter Brown

def area(width, height):
    return width * height

print(area(height=2, width=1))  # keyword args

```

```python
# lambda
x = lambda a: a + 10
print(x(5))                      # 15

x = lambda a, b: a * b
print(x(3, 4))                   # 12

```

Text Processing / Работа със стрингове ￼

```python
# Дефиниция
text = "hello, my name is Peter, I am 26 years old"
lst = text.split(", ")
# ['hello', 'my name is Peter', 'I am 26 years old']

# str()
x = str(3.5)                     # "3.5"

# Обратни/повторения
print("Hello" + "World")         # HelloWorld
print("red" * 3)                 # redredred

```

```python
# Слайс (substring)
text = "My name is Peter"
name = text[-5:]                 # "Peter" (същото като text[11:])

# isdigit / isupper / islower / strip / replace
'1'.isdigit()        # True
'P'.isupper()        # True
'u'.islower()        # True

" hello ".strip()    # "hello"
"hello".upper()      # "HELLO"
"HeLLo".lower()      # "hello"

txt = "I like bananas"
print(txt.replace("bananas", "apples"))   # I like apples

```

```python
# Прости задачи
# Reverse Strings
text = input()
while text != "end":
    text_reversed = ""
    for ch in reversed(text):
        text_reversed += ch
    print(f"{text} = {text_reversed}")
    text = input()

# Repeat Strings
strings = input().split(" ")
result = ""
for word in strings:
    length = len(word)
    result += word * length
print(result)

```

```python
# Substring – махане на всички срещания
first = input()
second = input()
while first in second:
    second = second.replace(first, "")
print(second)

```

Dictionaries / Речници (Maps) ￼

```python
# Създаване
my_dict = {}                                     # празен
my_dict = {"fruit": "apple", "vegetable": "cucumber"}

# чрез dict()
dict_arguments = dict(name="George", age=22)
# {"name": "George", "age": 22}

# много редове
my_dict = {
    "fruit": "apple",
    "vegetable": "cucumber",
    "diary": "milk",
}

```

```python
# Достъп и промяна
my_dict = {"name": "Jack", "age": 26}
print(my_dict["name"])          # Jack
print(my_dict.get("age"))       # 26
print(my_dict.get("address"))   # None

my_dict["age"] = 27             # update
my_dict["city"] = "Sofia"       # нов ключ

```

```python
# Итериране
squares = {1: 1, 2: 4, 3: 9}

for key in squares.keys():
    print(key, end=" ")

for value in squares.values():
    print(value, end=" ")

for key, value in squares.items():
    print(f"Key: {key}, Value: {value}")

```

```python
# Проверка за наличие
my_dict = {"name": "Peter", "age": 22}
if "name" in my_dict:
    print(my_dict["name"])

if 22 in my_dict.values():
    print("22 is a value in the dictionary")

```

```python
# Полезни методи
my_dict.clear()
copied = my_dict.copy()
val = my_dict.pop("fruit")      # връща стойността
k, v = my_dict.popitem()        # последна двойка (key, value)
del my_dict["course"]           # маха по ключ

```

Regular Expressions / Регулярни изрази ￼

```python
import re

# Прости класове
# \d  – цифра
# \D  – не-цифра
# \s  – интервал
# \S  – не- интервал
# \w  – буква/цифра/_
# \W  – всичко различно от горното
# ^ и $ – начало / край на реда
# [] – множества, [A-Z], [a-z], [0-9], [A-Za-z], [^aeiou]

```

```python
# Основни методи
text = input()

# findall – всички съвпадения → list
matches = re.findall(r"\d+", text)

# search – първо съвпадение → Match или None
m = re.search(r"\s", "The rain in Spain")
print(m.start())

# split – сплит по regex
parts = re.split(r"\s", "The rain in Spain")  # ['The','rain','in','Spain']

```

```python
# Match Full Name – "Име Фамилия"
names = input()
regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(regex, names)
print(" ".join(matches))

```

```python
# Match Dates с именувани групи
pattern = r"\b(?P<day>\d{2})([-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
text = input()
for match in re.finditer(pattern, text):
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")

```

Objects and Classes / Обекти и класове ￼

```python
# Дефиниране на клас
class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

```

```python
# Създаване на обект (инстанция на класа)
me = Person("Peter", "Johnson", 25)

print(me.first_name)   # Peter
print(me.last_name)    # Johnson
print(me.age)          # 25

# Промяна на атрибут
me.age += 1
print(me.age)          # 26

```

```python
# Пример: Comment
class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

```

```python
# Пример: Party
class Party:
    def __init__(self):
        self.people = []

party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

```

```python
# Класови атрибути и инстанционни методи
class Person:
    species = "mammal"            # класов атрибут – споделен

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name   # инстанционни
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

me = Person("Peter", "Johnson", 64)
print(me.species)                 # mammal
print(me.get_full_name())         # Peter Johnson

```
