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

def clear_console():
    os.system('clear')

def read_words():#Read data file of words
    words = []
    with open("./data.txt", "r",encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n","")
            words.append(line)
    return words

def fill_character(ch , word , result):
    for i in range(len(word)):
        if(unidecode.unidecode(word[i].lower()) == ch):
            result[i] = word[i] 

def run():
    clear_console()
    words = read_words() #Words to play
    lives = 5 #Player lives
    word = words[random.randint(0,len(words))] #Random word to play
    word_splited = list(word)
    word_result = list(map(lambda under: "_", word_splited))
    print(word)
    while(word_result!=word_splited):
        print("GUESS THE WORD")
        print(word_result)
        ch = input("Enter a letter: ")
        try:
            if len(ch)!=1 or ch.isnumeric():
                raise ValueError("Please, only use letters")
            fill_character(unidecode.unidecode(ch.lower()), word_splited, word_result)
        except ValueError as ve:
            print(ve)
        

    print("*******FIN DEL JUEGO*******")
    print("The word was: "+ word)

    
    


if __name__ == "__main__":
    run()