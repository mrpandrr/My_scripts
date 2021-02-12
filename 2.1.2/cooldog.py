a_z = 'abcdefghijklmnopqrstuvwxyz'
pasw = 'dogdogdog'
tests = 0
guess = ''
azlen = len(a_z)

for i in range(azlen):
    for j in range(azlen):
        for k in range(azlen):
            guess = a_z[i] + a_z[j] + a_z[k]
            tests += 1
            if guess == pasw:
                print('Got "{}" after {} tests'.format(guess, str(tests)))
                break

input()