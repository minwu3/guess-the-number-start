#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
import replit 


def difficulty_choose():  
  difficulty_mood = True 
  while difficulty_mood:
    difficulty = input("Choose a difficulty! Type 'easy' or 'hard': ")
    if difficulty == 'easy' or difficulty == 'e':
      attempts = 10
      difficulty_mood = False
    elif difficulty == 'hard' or difficulty == 'h':
      attempts = 5
      difficulty_mood = False
    else:
      print("Wrong type, type again.")
  return attempts
  

def the_chosen_number():
  the_number = random.randint(1, 100)
  return the_number


def the_guess_number():
  guess_number = input("Make a guess: ")
  
  return int(guess_number)

def play_game():
  print(art.logo)

  welcome_word = """
  Welcome to the Number Guessing Game!
  Guess a number between 1 and 100.
  """
  print(welcome_word)
  attempts = difficulty_choose()
  another_chance = True
  pick_a_number = the_chosen_number()
  
  while another_chance:
    print(f"You have {attempts} attempts remaining to guess the number!")
    the_guess = the_guess_number()
    if the_guess == pick_a_number:
      another_chance = False
      print("You got it!!! 👑👑👑")
    elif the_guess > pick_a_number:
      print("Too High.")
      attempts -= 1
    else:
      print("Too Low.")
      attempts -= 1


    if attempts <= 0:
      another_chance = False
      print(f"O-oh, no more chance... the number is {pick_a_number}")


    
while input("Start the game? Type 'y' to start! 😎 ") == 'y':
  replit.clear()
  play_game()
    
    
