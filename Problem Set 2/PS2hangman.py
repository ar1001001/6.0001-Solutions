# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    ls = list(secret_word)
    if letters_guessed == []:
        return False
    else:
        for i in letters_guessed:
            not_found = True
            for j in ls:
                if j==i:
                    not_found = False
                    break
            if not_found:
                return False
        return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ls = list(secret_word)
    lx = []
    lx.extend(['_ ']*len(ls))
    for i in range(len(ls)):
        for j in range(len(letters_guessed)):
            if ls[i] == letters_guessed[j]:
                lx[i]=ls[i]
    s = (''.join(lx))
    return s



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    l1 = list(string.ascii_lowercase)
    l2 = l1[:]
    for i in range(len(l2)):
        for j in range(len(letters_guessed)):
            if l2[i] == letters_guessed[j]:
                l1.remove(l2[i])
                break
    s = ''.join(l1)
    return s
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    w = secret_word
    unique = []
    for char in w[::]:
        if char not in unique:
            unique.append(char)
    print('Welcome to Hangman!')
    print('I am thinking of a word that is' , len(w), 'letters long.')
    lg = []
    lg2 = []
    lg3 = []
    print(get_guessed_word(w,lg))
    guessl = 6
    warns = 3
    print('You have', warns,'warnings left.')
    print('_________________________________')
    while guessl >= 0 :
        if len(lg)==len(list(w)):
            print('Congratulations, you won! ')
            print('Your total score is:', guessl*len(unique))
            break
        print('You have',guessl,' guesses left.')
        print(get_available_letters(lg))
        print('____________________________________')
        x = str(input('Please guess a letter:'))
        y = str.lower(x)
        lg.append(y)
        lg2.append(y)
        if y in lg3:
            lg.pop()
            print('You have input the same letter again!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif len(list(y)) >1:
            lg.pop()
            print('You have input more than one letter!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif str.isalpha(x) == False:
            lg.pop()
            print(' Oops! That is not a valid letter.')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:',get_guessed_word(w,lg2))
        
        elif is_word_guessed(w,lg) == True:
            print('Good guess!', get_guessed_word(w,lg2))
            
        elif is_word_guessed(w,lg) == False:
            if guessl == 1:
                print('Sorry, you ran out of guesses. The word was', w)
                break
            else:
                guessl -= 1
                lg.pop()
                print('Oops. That letter is not in my list.',get_guessed_word(w,lg2))
        lg3.append(y)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    same = False
    if list(my_word) == []:
        return False
        
    else:
        v = my_word.replace(' ','')
        s = list(v)
        o = list(other_word)
        if len(s) == len(o):
            for i in range(len(s)):
                if s[i] != '_': 
                    if s[i]==o[i]:
                        same = True
                    else:
                        return False
                        break
                else:
                    u = o[i]
                    for j in range(len(s)):
                        if s[j]==u:
                            return False
                            break
    if same:
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    w = []
    for g in wordlist:
        if match_with_gaps(my_word,g) == True:
            w.append(g)
    if w == [] or list(my_word) == []:
        return 'No matches found.'
    else:
        return w



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    w = secret_word
    unique = []
    for char in w[::]:
        if char not in unique:
            unique.append(char)
    print('Welcome to Hangman!')
    print('I am thinking of a word that is' , len(w), 'letters long.')
    lg = []
    lg2 = []
    lg3 = []
    print(get_guessed_word(w,lg))
    guessl = 6
    warns = 3
    print('You have', warns,'warnings left.')
    print('_________________________________')
    while guessl >= 0 :
        if get_guessed_word(w,lg2) == w:
            print('Congratulations, you won! ')
            print('Your total score is:', guessl*len(unique))
            break
        print('You have',guessl,' guesses left.')
        print(get_available_letters(lg))
        print('____________________________________')
        x = str(input('Please guess a letter:'))
        y = str.lower(x)
        lg.append(y)
        lg2.append(y)
        if y in lg3 and y != '*':
            lg.pop()
            print('You have input the same letter again!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif y == '*':
            lg.pop()
            k = get_guessed_word(w,lg2)
            print('Possible matches are,',show_possible_matches(k))
        elif len(list(y)) >1:
            lg.pop()
            print('You have input more than one letter!')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:', get_guessed_word(w,lg2))
        elif str.isalpha(x) == False:
            lg.pop()
            print(' Oops! That is not a valid letter.')
            if warns == 0:
                print('You have zero warnings left. You will now lose a guess!')
                guessl -= 1
            else:
                warns -= 1
                print('You have', warns,'warnings left:',get_guessed_word(w,lg2))
        
        elif is_word_guessed(w,lg) == True:
            print('Good guess!', get_guessed_word(w,lg2))
            
        elif is_word_guessed(w,lg) == False:
            if guessl == 1:
                print('Sorry, you ran out of guesses. The word was', w)
                break
            else:
                guessl -= 1
                lg.pop()
                print('Oops. That letter is not in my list.',get_guessed_word(w,lg2))
        lg3.append(y)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
