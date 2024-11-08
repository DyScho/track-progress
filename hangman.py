# in my third project I made a gallows game where you can guess multiple words and it can also end in a game over enjoy !!!

print('-=-=-=-=-=-=-=-=-=')
print('Welcome by hangman')
print('-=-=-=-=-=-=-=-=-=')

wordlist = ['youtube','python','javascript','c++','css','html','programeren','course']

allowed_e = 5
guesses = []
done = False
secret_w = random.choice(wordlist) 
opniew = True 

while opniew: 
    while not done:
        for letter in secret_w:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print(" _ ", end='' )
        print("")

        guess = input(f'you got that many lives {allowed_e} over. pick the next letter : ')
        guesses.append(guess.lower())
        if guess.lower() not in secret_w:
            allowed_e -= 1 
            if allowed_e == 0:
                print(f'nex time better ! the word was : {secret_w} !!')
                break
    
        done = True 
        for letter in secret_w:
            if letter not in guesses:
                done = False

        if done:
            print(f"great job you find the word : {secret_w}")
   
        print('see you next time !!')
