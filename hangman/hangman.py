import random


def greet_the_player() -> str:
    print(' '.join('HANGMAN'))
    return input('Guess the word:').strip()


def choose_random_word(_list_of_words: list) -> str:
    return random.choice(_list_of_words)


def is_right_word(_user_word: str, _random_word: str) -> str:
    if _user_word == _random_word:
        return 'You survived!'
    return 'You lost!'


list_of_words = ['python', 'java', 'swift', 'javascript']
random_word = choose_random_word(list_of_words)
user_word = greet_the_player()
result = is_right_word(user_word, random_word)
print(result)
