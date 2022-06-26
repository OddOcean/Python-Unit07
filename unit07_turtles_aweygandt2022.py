############################################################
#     Aidan Weygandt                        05.17.21       #
#     Unit 7 Problems                                      #
#     Turtle hangman                                       #
############################################################


import random
import turtle
hm = turtle.Turtle()
hm.speed(0)
num = 0
def hangman(num):
  if num == 1: #activates on first call
    hm.penup()
    hm.goto(0, 50)
    hm.pendown()
    hm.circle(25)
    hm.penup()
  elif num == 2: #activates on second call
    hm.goto(0, 50)
    hm.pendown()
    hm.goto(0, 0)
    hm.penup()
  elif num == 3: #activates on third call
    hm.goto(0, 40)
    hm.pendown()
    hm.goto(-40, 30)
    hm.penup()
  elif num == 4: #activates on fourth call
    hm.goto(0, 40)
    hm.pendown()
    hm.goto(40, 30)
    hm.penup()
  elif num == 5: #activates on fifth call
    hm.goto(0, 0)
    hm.pendown()
    hm.goto(-10, -60)
    hm.penup()
  elif num == 6: #activates on sixth call
    hm.goto(0, 0)
    hm.pendown()
    hm.goto(10, -60)
    hm.penup()
    hm.goto(-30, -75)
    hm.write("Game Over")
#for x in range(8):
  #drawHangman(x)
def toString(list):
    s = ""
    for e in list:
        s += e
    return s

words = ["kat", "berd", "paret", "lyon", "porkyoupine", "kanegaroo", "falcun", "pooma", "pidjon", "cobruh"]

while True:
  index = random.randint(0, len(words) - 1)
  hiddenWord = words[index]

  guessedWord = len(hiddenWord) * ['*']

  numberOfCorrectLettersGuessed = 0
  numberOfMisses = 0

  while numberOfCorrectLettersGuessed < len(hiddenWord):
    letter = input("(Guess) Enter a letter in word " + toString(guessedWord) + " > ").strip()

    if letter in guessedWord:
        print("\t", letter, "is already in the word")
    elif hiddenWord.find(letter) < 0:
        print("\t", letter, "is not in the word")
        numberOfMisses += 1
        hangman(numberOfMisses)
    else:
        k = hiddenWord.find(letter)
        while k >= 0:
            guessedWord[k] = letter
            numberOfCorrectLettersGuessed += 1
            k = hiddenWord.find(letter, k + 1)
    if numberOfMisses == 6: break #if 6 misses then game ends

  print("The word is " + hiddenWord + ". You missed "
          + str(numberOfMisses) + (" time" if (numberOfMisses <= 1) else " times"))

  anotherGame = input("Do you want to guess for another word? Enter y or n> ").strip()
  if anotherGame == 'n':
      print("Finished")
      break
  else: hm.clear() #clears hangman screen incase of second game
