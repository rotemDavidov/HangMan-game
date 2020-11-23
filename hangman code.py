from pathlib import Path #for cheacking if the file exist 

#HANGMAN_PHOTOS is a const dict each key conatain the stage in the game
HANGMAN_PHOTOS = {
"1":"x-------x",\
"2":"\
x-------x\n\
|\n\
|\n\
|\n\
|\n\
|",\
"3":"\
x-------x\n\
|       |\n\
|       0\n\
|\n\
|\n\
|",\
"4": "\
x-------x\n\
|       |\n\
|       0\n\
|       |\n\
|\n\
|",\
"5":"\
x-------x\n\
|       |\n\
|       0\n\
|      /|\\ \n\
|\n\
|",\
"6":"\
x-------x\n\
|       |\n\
|       0\n\
|      /|\\\n\
|      /\n\
|",\
"7":"\
x-------x\n\
|       |\n\
|       0\n\
|      /|\\\n\
|      / \\\n\
|"}




def print_hangman_logo():
    """print the hangman logo
    return: None """
    
    print("""
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
             __/ | 
            |___/ """) 
            
          
def hangman(file_path, index):
    """this function call all the function to start and play the game.
    :param file_path: path to file
    :param index: location of word in the file
    :type file: string
    :type index: int
    :return: None
    """
    #choosing the secret_word for gussing 
    secret_word = choose_word(file_path, index)
    #set the list of the letters the user gussing
    old_letters_guessed = []
    #set the num of tries the user make
    num_of_tries = 0
    print_stage_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    
    #starting the gussing , by using loop while the gussing not reached 6 and the user not win 
    while num_of_tries < 6 and not check_win(secret_word, old_letters_guessed):
        letter_guessed = input("Guess a letter: ")
        #while the user gussing wrongs input {while !false => while True}
        while not(try_update_letter_guessed(letter_guessed, old_letters_guessed)):
            letter_guessed = input("Guess a letter:")
        if letter_guessed.lower() not in secret_word:
            num_of_tries += 1
            print_stage_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed)) 
            
    #if we break the loop we will cheking : if num_of_tries < 6 we break the loop bcause the revel suucssed
    #else we break the loop because the num of tries reached 6    
    if num_of_tries < 6: 
        print("WIN")
    else:
        print("LOSE")
     
        
          
def choose_word(file_path, index):
    """this function check what is the word in index place
    param file_path:represents a path to the text file
    param index: represents the location of a particular word in the file
    type file_path : string
    type  index: int
    return: the word in the index
    rtype: string"""   
    
    #open the file
    cheack_file = open(file_path, "r")
    #creating list of words from the file
    list_from_file = []
    for line_with_enter in cheack_file.readlines():
        line = line_with_enter.strip() #delete the \n in the end of line
        list_from_file += line.split(" ") 

    #cheaking wich word in index 
    while(len(list_from_file) < index):  #while len(list_from_file) < index
    #If the index is greater than the number of words in the file, 
    #the loop continues to count locations in a circular
        index = index - len(list_from_file) - 1 
    word_by_index = list_from_file[index - 1]
    
    #close the file
    cheack_file.close()
    return  word_by_index           
            
def show_hidden_word(secret_word, old_letters_guessed):
    """the function revel the letter guessed in secret_word
    param secret_word: the word to be revealed
    param old_letters_guessed: the list to check in\
    type secret_word: string
    type old_letters_guessed: list
    return: the word after revel
    rtype: list"""
    reveal_list = ""
    for secret_letter in secret_word:
        if secret_letter in old_letters_guessed:
            reveal_list += secret_letter + " "
        else:
           reveal_list += "_ "
    return reveal_list             
            
def print_stage_hangman(num_of_tries):
    """this function print the num_of_tries+1 stage (num_of_tries == 0 is stage 1)
    param num_of_tries: the amount of wrong guesses
    type num_of_tries: int
    return: None """
    if num_of_tries == 0:
        print("lets start!\a")
    else:
        print(":(")
    print(HANGMAN_PHOTOS[str(num_of_tries+1)])

def check_valid_input(letter_guessed, old_letters_guessed):
    """this function check if the input is good according to conditions"
    :param letter_guessed: the user guess input
    :param old_letters_guessed: all the old  users guesses 
    :type letter_guessed: string
    :type check_valid_input: list
    :return: if the input is vaild and if the input was typed befor.
    :rtype: Bool"""
    
    if len(letter_guessed) > 1: #if the string contain 2 char or more
        return False
    elif not(letter_guessed.isalpha()): #if the input contain chars that not alpabet
        return False
    elif letter_guessed in old_letters_guessed: #if the input alredy typed befor
        return False
    else:
        return True  


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this function add the guess of the user to the list or not"
    :param letter_guessed: the user guess input
    :param old_letters_guessed: all the old  users guesses 
    :type letter_guessed: string
    :type check_valid_input: list
    :return: True/False if the adding suucssed
    :rtype: Bool"""
    #if check_valid_input return True 
    if(check_valid_input(letter_guessed.lower(), old_letters_guessed)):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed)) 
        return False
    
def check_win(secret_word, old_letters_guessed):
    """this function check if the secret_word contain
    all the letters in old_letters_guessed
    param secret_word: the word the user neet to guess
    param old_letters_guessed: the letters that the user alredy guessed
    type secret_word: string
    type old_letters_guessed: list
    return : the result of checking
    rtype: Bool"""
    
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False #if the letter not in old_letters_guessed we stop the loop
    return True #in case all the letter in secret word


def main():
    #printing the hangman logo
    print_hangman_logo()
    #ask a path to file from the user
    file_path = Path(input("Enter file path: ")) #using the path function to cheack if path is exist
    while not file_path.is_file():               #without open the file
        print(" OH ! NO ! WE GOT LOST")
        file_path = Path(input("Enter file path AGAIN: "))  
    #ask a index from the user and convert it to int
    index = int(input("Enter index: "))
    #calling the function hangman to start the game !
    hangman(file_path, index)
    
if __name__ == "__main__":
    main()
