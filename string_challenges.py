# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
vocals = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
sum = 0
for w in word:
    if w in vocals:
        sum += 1
print(sum)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
s_list = sentence.split()
print(len(s_list))



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
s_list = sentence.split()
for word in s_list:
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
s_list = sentence.split()
sum = 0
cnt = 0
for word in s_list:
    cnt += 1
    sum +=len(word)
print(sum/cnt)
