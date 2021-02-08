import time as ti
files = ['bin' , 'sys' , 'root', 'lib']
"""APPLICATIONS"""
def hangman_hangman():
  import random
  import time

  # Initial Steps to invite in the game:
  print("\nWelcome to Hangman game by DataFlair\n")
  name = input("Enter your name: ")
  print("Hello " + name + "! Best of Luck!")
  time.sleep(2)
  print("The game is about to start!\n Let's play Hangman!")
  time.sleep(3)
  def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    # A loop to re-execute the game when the first round ends:

  def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
  # Initializing all the conditions required for the game:
  def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


  main()

  hangman()

def guessing_game():
  import random
  number = random.randint(0,100)
  tries = 1
  done = False
  print("this is the number guessing game. enter a guess and see if you're right!")
  while True:
    guess = int(input("enter a guess"))
    if guess == number:
      done == True
      print("you won!")
      break
    else:
      tries += 1
      if guess > number:
        print("too large")
      else: 
        print("too small")
      if done == True:
        break
  print(f"you needed {tries} tries!")

def text():
  print('welcome To Text! a simple text editor')
  print('type "sys.back to go exit"')
  while True:
    x = input()
    if x == 'sys.back':
      break

def calc():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calc()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
def search():
  print('this is search, a simple web browser. \ntype "sys.back to exit"')
  while True:
    x = input('')
    if x == 'sys.back':
      break
    else:
      print(f'copy and paste this in your web browser: https://google.com/search?q={x}')

def timer():
  from time import sleep
  m = 0
  print("""**************************
  Welcome To FASTIMER®
  **************************""")
  while True:
    try:
        countdown = int(input("How many seconds:  "))
        break
    except ValueError:
        print("ERROR, TRY AGAIN")
  original = countdown
  while countdown >= 60:
    countdown -= 60
    m += 1
  for i in range (original,0,-1):
    if m < 0:
        break
    for i in range(countdown,-2,-1):
        if i % 60 == 0:
            m-=1
        if i == 0:
            break
        print(m," minutes and ",i," seconds")
        sleep(1)
    if m < 0:
        break
    for j in range(59,-1,-1):
        if j % 60 == 0:
            m-=1          
        print(m," minutes and ",j," seconds")
        sleep(1)
  print("TIMER FINISHED")

# login
def login():
  print("Steam Security Software ©")
  print("-------------------------")
  print("<<<<<<<<<Welcome>>>>>>>>>")
  username = input("Username:")
  if username == "admin123" :
    print ("Now type password")

  else :
    print ("please try another user name. This user name is incorrect")


  password = input ("Password:")
  if password  == "password456" and username == "admin123":
    print ("ACCESS  GRANTED")
    print ("<<Welcome Admin>>")
    #continue for thins like opening webpages or hidden files for access

  else :
    print ("INTRUDER ALERT !!!!" , "SYSTEM LOCKED")
    while True:
      print("intruder!!!")
login()

def mainOS():
  print('WELCOME TO PYTHON OPERATING SYSTEM. TYPE "CMD" FOR COMMANDS')
  H = False
  G = False
  while True:
    x = input('>>> ')
    if x == 'shutdown':
      print('shutting down...')
      ti.sleep(3)
      break
    elif x == 'open text':
      text()
    elif x == 'open calc':
      calc()
    elif x == 'open search':
      search()
    elif x == 'ls':
      for x in files:
        print(x)
    elif x == 'ls /bin':
      print('OS_credits.txt \n security.txt')
    elif x == 'read OS_credits.txt':
      print('''
      ***********CREDITS*************
      Roger - creator
      Roger - coder
      Lilian - second tester
      Roger - first updater
      Lilian - nfirst feedbacker

      ''')
    elif x == 'read security.txt':
      print('''
      <<SECURITY>>
      STEAM SECURITY SOFTWARE INC.
      ROGER - SECURITY TESTER
      SAFENESS - LV. 2(DECENT)
      ''')
    elif x =='ls /root':
      print('\n')
    elif x == 'pip install Guessing_Game':
      print('getting packages...')
      print('000%')
      ti.sleep(1)
      print('025%')
      ti.sleep(1)
      print('0.75')
      ti.sleep(3)
      print('100%: DONE: GUESSING_GAME IS INSTALLED. TYPE "open guessing game" TO OPEN.')
      G = True

    elif x == 'pip install Hangman':
      print('getting packages...')
      print('000%')
      ti.sleep(1)
      print('025%')
      ti.sleep(1)
      print('0.75')
      ti.sleep(3)
      print('100%: DONE: HANMAN IS INSTALLED. TYPE "open hangman" TO OPEN.')
      H = True
    elif x == 'open hangman':
      if H == True:
        hangman_hangman()
      else: 
        print('ERROR<hangman is not installed>')
    
    elif x == 'open guessing game':
      if G == True:
        guessing_game()
      else:
        print('ERROR<guessing game is not installed>')
    elif x == 'reboot':
      print('rebooting...')
      ti.sleep(1)
      login()
    elif x == 'CMD' or x == 'cmd':
      cmd = ['pip install [package name]- install a package', 'reboot - reboot the system' , 'open [app]- open a package ', 'ls [folder or directory]*- list all files in folder or directory', 'read [text file]- read a text file', 'shutdown - shutdown the system', '* this means the input is optional']
      for i in cmd:
        print(i)
    else:
      print('ERROR<THAT IS NOT A APP OR COMMAND IN PyOS>')
mainOS()
