word = input('Введите слова через пробел: ')
word_2 = word.split()
# for word_2 in enumerate (word_2, 1):
#     print(word_2[:10])

res = dict(list(enumerate(word_2, 1)))

for k, v in res.items():
    print(f'{k} - {v[:10]}')


