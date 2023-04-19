import random

from src.utils import print_error, print_grey, print_success, print_warning

random.seed(40)

class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10_000 ):
        self.word_len = word_len
        self.words = self.generate_word_frequency(file_path, word_len, limit)

    def generate_word_frequency(self, file_path, word_len: int, limit: int):
        # Build Data

        words_freq = []

        with open(file_path) as f:
            for line in f:
                word, frequency = line.split(',')
                frequency = int(frequency)

                words_freq.append((word, frequency))

        # Filter Data
        words_freq = list(filter(lambda w_freq: len(w_freq[0]) == word_len, words_freq))



        # Sort Data
        words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)


        # Limit Data
        words_freq = words_freq[:1000]


        #Drop Frequency
        words = [w_freq[0] for w_freq in words_freq]

        return words

    def run(self, ):
        #Random Word
        word = random.choice(self.words)
        word = word.upper()


        #Start Game
        num_try = 6
        success = False

        while num_try:
            guess_word = input (f"Enter a {self.word_len} letter word or 'q' to EXIT:")
            if guess_word.lower() == 'q':
                print()
                print ('Qitted!')
                break
            guess_word = guess_word.upper()

            #word lenght
            if len(guess_word) != self.word_len:
                print()
                print (f'Please try again with a {self.word_len} letter word! You entered "{len(guess_word)}"')
                print()

            #check valid word
            if guess_word.lower() not in self.words:
                print()
                print_error('Word is not valid!')
                print()
                continue

            #check valid, invalid positions, invalid charachters
            for w_letter, g_letter in zip(word, guess_word):
                if w_letter == g_letter:
                    print_success(f' {w_letter} ', end=' ')


                elif g_letter in word:
                    print_warning(f' {g_letter} ', end=' ')


                else:
                    print_error(f' {g_letter} ', end=' ')

            print()

            #check success
            if word == guess_word:
                print('')
                print_success('Congratulations')
                success = True

                break




            num_try -=1

        if not success:
            print_warning(f'Game Over!!! The word was "{word}"!')

