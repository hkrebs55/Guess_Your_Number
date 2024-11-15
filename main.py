# The computer will try to guess the number you are guessing in 10 turns or less
import random

print("I bet I can guess your number in 10 guesses or less. "
      "All you need to tell me is if I the number I guess is too high or too low. \n"
      "Pick a number from 1 to 100. Don't tell me.")

correct_num = False
tries = 0


def guess_number(min_num, max_num):
      global correct_num
      global tries
      if tries >= 10:
            print("Bummer I did not get the number you were thinking. I'm sure I will guess it next time.")
            return
      if correct_num != True:
            guessed_num = random.randrange(min_num, max_num)
            print("I am guessing your picked number is " + str(guessed_num) +
                  ". Am I correct? Please type in 'Y' for yes, 'H' for too high, or 'L' for too low.")
            am_correct = input()
            if am_correct == "Y":
                  print("I knew I could guess your number! Better luck next time.")
                  return correct_num == True
            elif am_correct == "L":
                  tries += 1
                  if tries < 10:
                        print("Hmmmmmm.....Okay")
                  return guess_number(guessed_num + 1, max_num)
            elif am_correct == "H":
                  tries += 1
                  if tries < 10:
                        print("Hmmmmmm.....Okay")
                  return guess_number(min_num, guessed_num)


guess_number(1, 101)
