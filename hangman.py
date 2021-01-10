filled_array = list(input('Pick your word = '))
empty_array = ['_'] * len(filled_array)

letters_guessed =[]


counter = 0
while counter != 5 and empty_array.count('_') != 0:
    first_letter_guess = input('Type in a letter you think is included in the word. ')
    if first_letter_guess in letters_guessed:
        print("You guessed this letter once already.")
    elif len(first_letter_guess) != 1:
        print("Please enter only 1 letter.")
    else:
        if first_letter_guess in filled_array:
            for i, j in enumerate(filled_array):
                if j == first_letter_guess:
                    empty_array[i] = filled_array[i]

            print(empty_array)
        else:
            counter += 1
            print('Your letter is not included in the word. Try again. You have ' + str(5 - counter) + ' tries left.')
    letters_guessed.append(first_letter_guess)


if counter == 5:
    print('You lost.')
else:
    print('Congratulations! You win.')
