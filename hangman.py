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


def read_words():#Read data file of words
    words = []
    with open("./data.txt", "r",encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n","")
            words.append(line)
    return words


def run():
    words = read_words() #Words to play
    lives = 5 #Player lives

    while(lives > 0 ):
        pass
    print("*******FIN DEL JUEGO*******")

    
    


if __name__ == "__main__":
    run()