import random
words = ['Самовар','Весна','Лето']
word = random.choice(words)
letter = random.choice(word)
index_letter = word.index(letter)
word_with_symbol = list(word)
word_with_symbol[index_letter] = '?'
print('Игра отгадай букву. \nЗагаданное слово: ',"".join(word_with_symbol))
a = input('Введите свой вариант: ')
if a == letter:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз')
