import random
import string 
print('Welcome to Password Maker!')
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red','orange', 'yellow', 'green','blue', 'purple', 'fluffy','white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda', 'cat','wolf']
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char 
    print('Your new password is: %s' % password)

    option = input('Would you like another password? Type y or n: ') #ask user input
    if option =='n':
        break
        
