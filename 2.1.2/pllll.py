ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def brute_force_guesser(passwd, guess = ''):
    global _bfg_counter
    if len(guess) == 0:
        _bfg_counter = 0
    if len(guess) == len(passwd):
        _bfg_counter += 1
        if guess == passwd:
            print('Got "{}" after {} tests'.format(guess, str(_bfg_counter)))
            return True
        return False
    else:
        for c in ALPHABET:
            print(guess)
            if brute_force_guesser(passwd, guess + c):
                return True
        return False

brute_force_guesser('salim')    # => Got "dog" after 2399 tests
brute_force_guesser('doggy')  # => Got "doggy" after 1621229 tests
