# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
flist = {}
for i in range(len(students)):
    #print(students[i]['first_name'])
    if students[i]['first_name'] in flist:
        flist[students[i]['first_name']] +=1
    else:
        flist.update({students[i]['first_name']:1})
for k, v in flist.items():
    print(f'{k}: {v}')



# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
flist = {}
max_val = 0
max_name = 0
for i in range(len(students)):
    if students[i]['first_name'] in flist:
        flist[students[i]['first_name']] +=1
    else:
        flist.update({students[i]['first_name']:1})
    if flist[students[i]['first_name']] > max_val:
        max_val = flist[students[i]['first_name']]
        max_name = students[i]['first_name']
print(f'Самое частое имя среди учеников: {max_name}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
s_flist = []
s = 0
for students in school_students:
    flist = {}
    max_val = 0
    max_name = 0
    for i in range(len(students)):
        if students[i]['first_name'] in flist:
            flist[students[i]['first_name']] +=1
        else:
            flist.update({students[i]['first_name']:1})
        if flist[students[i]['first_name']] > max_val:
            max_val = flist[students[i]['first_name']]
            max_name = students[i]['first_name']
    s_flist.insert(s, max_name)
    s += 1
for i in range(len(s_flist)):
    print(f'Самое частое имя в классе {i+1}: {s_flist[i]}')
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for classes in school:
    male = 0
    female = 0
    #print(f"В классе {classes['class']}")
    for students in classes['students']:
        if is_male[students['first_name']]:
            male += 1
        else:
            female += 1
        #print(students['first_name'])
    print(f"В классе {classes['class']} {female} девочки и {male} мальчика")
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
m_class = {}
f_class = {}
for classes in school:
    male = 0
    female = 0
    #print(f"В классе {classes['class']}")
    for students in classes['students']:
        if is_male[students['first_name']]:
            male += 1
        else:
            female += 1
        #print(students['first_name'])
    m_class.update({classes['class']:male})
    f_class.update({classes['class']:female})
    print(f"В классе {classes['class']} {female} девочки и {male} мальчика")
max_v = 0
max_cls = ''
for k, v in m_class.items():
    if v > max_v:
        max_c = v
        max_cls = k
print(f'Больше всего мальчиков в классе {max_cls}')
for k, v in f_class.items():
    if v > max_v:
        max_c = v
        max_cls = k
print(f'Больше всего девочек в классе {max_cls}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a