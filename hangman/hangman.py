import random


def greet_the_player(_word_with_hidden_letters: str) -> str:
    print(' '.join('HANGMAN'))
    return input(f'Guess the word {_word_with_hidden_letters}:').strip()


def replace_chars(_random_word: str) -> str:
    return _random_word[:3] + '-' * (len(_random_word) - 3)


def check_word(_user_word: str, _random_word: str) -> str:
    if _user_word == _random_word:
        return 'You survived!'
    return 'You lost!'


list_of_words = ['python', 'java', 'swift', 'javascript']
random_word = random.choice(list_of_words)
word_with_hidden_letters = replace_chars(random_word)
user_word = greet_the_player(word_with_hidden_letters)
result = check_word(user_word, random_word)
print(result)
