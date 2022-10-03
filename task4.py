# Пам-парам парам-пам парам

with open('task4.txt', 'r', encoding='utf8') as file:
    verse = file.read()

vowels = 'а у о и э ы я ю е ё'.split()

phrase = verse.split()
number_of_vowels = [sum(letter in vowels for letter in word)for word in phrase]

print(number_of_vowels)

with open('task4.txt', 'a', encoding='utf8') as file:
    if len(set(number_of_vowels)) == 1:
        file.write('\nПарам пам-пам')
    else:
        file.write('\nПам парам')
