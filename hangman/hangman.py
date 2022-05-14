import random


def open_char(_word_with_hidden_letters: str, _random_word: str, _user_input: str) -> str:
    result = ''
    for i in range(len(_random_word)):
        if _random_word[i] == _user_input:
            result += _random_word[i]
        else:
            result += _word_with_hidden_letters[i]
    return result


def replace_chars(_random_word: str) -> str:
    return _random_word[:0] + '-' * len(_random_word)


def check_word(_user_word: str, _random_word: str) -> str:
    if _user_word == _random_word:
        return 'You survived!'
    return 'You lost!'


list_of_words = ['python', 'java', 'swift', 'javascript']
random_word = random.choice(list_of_words)
random_word_set = set(random_word)
word_with_hidden_letters = replace_chars(random_word)
print(' '.join('HANGMAN'), '\n')
for _ in range(8):
    print(word_with_hidden_letters)
    user_input = input('Input a letter:').strip()
    if user_input in random_word_set:
        word_with_hidden_letters = open_char(word_with_hidden_letters, random_word, user_input)
    else:
        print("That letter doesn't appear in the word.")
print('\n' + 'Thanks for playing!')
