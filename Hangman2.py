import random, string
wordbank = ['fuzzy', 'hair', 'trade', 'substance', 'wind', 'zoo', 'scared', 'multiply', 'enthusiastic', 'building', 'gusty', 'jewel', 'sordid', 'joke', 'admire', 'useless', 'view', 'cushion', 'glow', 'peep', 'consider', 'simplistic', 'neck', 'tramp', 'rose']
letter_bank = [x for x in string.ascii_uppercase()]
uppercase = letter_bank
inputword = random.choice(wordbank)
letterlist = [letter for letter in inputword]
newlist = letterlist
counter = 0
lettersguessed = []
def replace_letters():
    global counter
    global lettersguessed
    playerfriendlylist = ["_" if x not in uppercase else x for x in newlist]
    if playerfriendlylist == newlist:
        counter = 6
    if counter < 6:
        print("you have " + str(5-counter) + " guesses left")
        if counter == 0:
            print("""
  +---+
  |   |
      |
      |
      |
      |
=========
        """)
            print(playerfriendlylist)
            print("You have guessed the letters: " + str(lettersguessed))
        if counter == 1:
            print("""
 +---+
  |   |
  O   |
      |
      |
      |
=========        
        """)
            print(playerfriendlylist)
            print("You have guessed the letters: " + str(lettersguessed))
        if counter == 2 :
            print("""
+---+
  |   |
  O   |
 /|   |
      |
      |
=========        
        """)
            print(playerfriendlylist)
            print("You have guessed the letters: " + str(lettersguessed))
        if counter == 3:
            print("""
+---+
  |   |
  O   |
 /|\  |
      |
      |
=========        
        """)
            print(playerfriendlylist)
            print("You have guessed the letters: " + str(lettersguessed))
        if counter == 4:
            print("""
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========        
        """)
            print(playerfriendlylist)
            print("You have guessed the letters: " + str(lettersguessed))
        print("guess a letter")
        biginput = input().lower()
        if biginput in newlist and biginput.upper() in letter_bank:
            letterindexes = [n for n,x in enumerate(newlist) if x == biginput]
            for index in letterindexes:
                newlist[index] = biginput.upper()
            letter_bank.pop(letter_bank.index(biginput.upper()))
        else:
            counter += 1
            if biginput in lettersguessed:
                pass
            else:
                lettersguessed.append(biginput)
while counter < 5:
    replace_letters()
if counter == 5:
    print("""
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========  
           (`-')  _ <-. (`-')   (`-')  _                     (`-') (`-')  _   (`-') ,---. 
    .->    (OO ).-/    \(OO )_  ( OO).-/         .->        _(OO ) ( OO).-/<-.(OO ) |   | 
 ,---(`-') / ,---.  ,--./  ,-.)(,------.    (`-')----. ,--.(_/,-.\(,------.,------,)|   | 
'  .-(OO ) | \ /`.\ |   `.'   | |  .---'    ( OO).-.  '\   \ / (_/ |  .---'|   /`. '|   | 
|  | .-, \ '-'|_.' ||  |'.'|  |(|  '--.     ( _) | |  | \   /   / (|  '--. |  |_.' ||  .' 
|  | '.(_/(|  .-.  ||  |   |  | |  .--'      \|  |)|  |_ \     /_) |  .--' |  .   .'`--'  
|  '-'  |  |  | |  ||  |   |  | |  `---.      '  '-'  '\-'\   /    |  `---.|  |\  \ .--.  
 `-----'   `--' `--'`--'   `--' `------'       `-----'     `-'     `------'`--' '--'`--'    
    """)
    print("Game over!")
    print("The word was \"{}\".".format(inputword))
if counter == 6:
    print(newlist)
    print("""
 +---+
      |
      |
  O   |
 /|\  |
 / \  |
=========

  ___    ___ ________  ___  ___          ___       __   ___  ________   ___       
 |\  \  /  /|\   __  \|\  \|\  \        |\  \     |\  \|\  \|\   ___  \|\  \      
 \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \    \ \  \ \  \ \  \\ \  \ \  \     
  \ \    / / \ \  \\\  \ \  \\\  \       \ \  \  __\ \  \ \  \ \  \\ \  \ \  \    
   \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \|\__\_\  \ \  \ \  \\ \  \ \__\   
 __/  / /      \ \_______\ \_______\       \ \____________\ \__\ \__\\ \__\|__|   
|\___/ /        \|_______|\|_______|        \|____________|\|__|\|__| \|__|   ___ 
\|___|/                                                                      |\__\
                                                                             \|__|
                                                                                      
    """)

def wait():
    while 1 == 1:
        pass
wait()
