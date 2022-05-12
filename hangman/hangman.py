def greet_the_player() -> str:
    print(' '.join('HANGMAN'))
    return input('Guess the word:').strip()


def is_right_word(word: str) -> str:
    if word == 'python':
        return 'You survived!'
    return 'You lost!'


user_word = greet_the_player()
print(is_right_word(user_word))
