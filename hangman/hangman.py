import random
import string


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


def check_success(_user_word: str, _random_word: str) -> str:
    if _user_word == _random_word:
        return f'\nYou guessed the word {_user_word}!\nYou survived!'
    return 'You lost!'


def check_correct_input(_user_input: str, _english_alphabet: str, _chars_set: set) -> str:
    if len(_user_input.strip()) > 1 or len(_user_input.strip()) == 0:
        return 'Please, input a single letter.'
    if _user_input not in _english_alphabet:
        return 'Please, enter a lowercase letter from the English alphabet.'
    if _user_input in _chars_set:
        return "You've already guessed this letter."


def choose_action() -> str:
    return input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:').strip()


print(' '.join('HANGMAN'), '\n')
times_win = 0
times_loss = 0
while True:
    action = choose_action()
    if action == 'play':
        list_of_words = ['python', 'java', 'swift', 'javascript']
        english_alphabet = string.ascii_lowercase
        random_word = random.choice(list_of_words)
        random_word_set = set(random_word)
        word_with_hidden_letters = replace_chars(random_word)
        chars_set = set()
        attempts = 8
        while attempts > 0:
            print(word_with_hidden_letters)
            user_input = input('Input a letter:').strip()
            check_result = check_correct_input(user_input, english_alphabet, chars_set)
            if check_result:
                print(check_result)
            else:
                if user_input in random_word_set:
                    word_with_hidden_letters = open_char(word_with_hidden_letters, random_word, user_input)
                    chars_set.add(user_input)
                else:
                    print("That letter doesn't appear in the word.")
                    chars_set.add(user_input)
                    attempts -= 1
            if word_with_hidden_letters == random_word:
                break
        check_win_loss = check_success(word_with_hidden_letters, random_word)
        print(check_win_loss)
        if check_win_loss == 'You lost!':
            times_loss += 1
        else:
            times_win += 1
    if action == 'results':
        print(f'You won: {times_win} times.\nYou lost: {times_loss} times.')
    if action == 'exit':
        break
exit()
