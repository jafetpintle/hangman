from pickle import FALSE, TRUE
import random
import os
import unidecode

#Hangman art by chrishorton
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

END_MESSAGES = ['''
  #####  ####### #     #  #####  ######     #    #######  #####  
 #     # #     # ##    # #     # #     #   # #      #    #     # 
 #       #     # # #   # #       #     #  #   #     #    #       
 #       #     # #  #  # #  #### ######  #     #    #     #####  
 #       #     # #   # # #     # #   #   #######    #          # 
 #     # #     # #    ## #     # #    #  #     #    #    #     # 
  #####  ####### #     #  #####  #     # #     #    #     #####  
                                                                 
 #     # ####### #     #    #     # ####### #     #    ###       
  #   #  #     # #     #    #  #  # #     # ##    #    ###       
   # #   #     # #     #    #  #  # #     # # #   #    ###       
    #    #     # #     #    #  #  # #     # #  #  #     #        
    #    #     # #     #    #  #  # #     # #   # #              
    #    #     # #     #    #  #  # #     # #    ##    ###       
    #    #######  #####      ## ##  ####### #     #    ###       
                                                                 
''','''
           #####  ####### ######  ######  #     #           
          #     # #     # #     # #     #  #   #            
          #       #     # #     # #     #   # #             
           #####  #     # ######  ######     #              
                # #     # #   #   #   #      #              
          #     # #     # #    #  #    #     #              
           #####  ####### #     # #     #    #              
                                                            
 #     # ####### #     #    #       #######  #####  ####### 
  #   #  #     # #     #    #       #     # #     # #       
   # #   #     # #     #    #       #     # #       #       
    #    #     # #     #    #       #     #  #####  #####   
    #    #     # #     #    #       #     #       # #       
    #    #     # #     #    #       #     # #     # #       
    #    #######  #####     ####### #######  #####  ####### 
                                                            
''' ]

HANGMAN = '''
                                                                                 
 #    #   ##   #    #  ####  #    #   ##   #    #     ####    ##   #    # ###### 
 #    #  #  #  ##   # #    # ##  ##  #  #  ##   #    #    #  #  #  ##  ## #      
 ###### #    # # #  # #      # ## # #    # # #  #    #      #    # # ## # #####  
 #    # ###### #  # # #  ### #    # ###### #  # #    #  ### ###### #    # #      
 #    # #    # #   ## #    # #    # #    # #   ##    #    # #    # #    # #      
 #    # #    # #    #  ####  #    # #    # #    #     ####  #    # #    # ###### 
                                                                                 '''

def clear_console():
    os.system('clear')

def read_words():#Read data file of words
    words = []
    with open("./data.txt", "r",encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n","")
            words.append(line)
    return words

def exist_character(ch , word , result): #Check if character exist and fill it in the list
    ch_flag = False #Flag to check if character exists in the word
    for i in range(len(word)):
        if(unidecode.unidecode(word[i].lower()) == ch):
            result[i] = word[i]
            ch_flag = True
    return ch_flag
        

def run():
    clear_console()
    words = read_words() #Words to play
    tries = 0 #Player tries
    word = words[random.randint(0,len(words))] #Random word to play
    word_splited = list(word)
    word_result = list(map(lambda under: "_", word_splited))
    while(word_result!=word_splited and tries < 6):
        print(HANGMAN)
        print(HANGMANPICS[tries])
        print(word_result)
        ch = input("Enter a letter: ")
        try:
            if len(ch)!=1 or ch.isnumeric():
                raise ValueError("Please, only use letters")
            if(not exist_character(unidecode.unidecode(ch.lower()), word_splited, word_result)):
                tries+=1
        except ValueError as ve:
            print(ve)
        clear_console()
    
    if(tries < 6):
        print(END_MESSAGES[0])
    else:
        print(END_MESSAGES[1])
    print(HANGMANPICS[tries])
    print("The word was: "+ word)

    
    


if __name__ == "__main__":
    run()