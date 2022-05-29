import sys
import random
name = input("What is your name?\n")
def run():
  print(f"Hello, {name}, let's play hangman!")
  print("The word below. Start guessing letters...")
  #Defining the bag of words
  bag_of_words = ["sentence", "country", "wedding", "bloody", "between", "drawing", "animal", "together", "picture", "laptop", "mother", "musical", "second", "mountain", "exception", "before", "chocolate", "singer", "football", "newspaper", "friendship", "cigarette", "television", "environment", "chicken", "information", "science", "mathematics", "school", "interantional", "promotion", "refrigerator", "student", "pollution", "delivery", "benefit", "outside", "unique", "insane", "sweatshirt", "sleeves", "backpack", "lighter", "coding", "chairs", "poster", "smartphone", "keyboard", "guitar", "shoulders", "finger", "swimming", "exercise", "cushion"]
  d = 0
  for char in word:
      if char in guesses:
        print(char)
      else:word = random.choice(bag_of_words)
  guesses = " "
  turns = 10
  while turns > 0:
    faile
        print("_")
        failed += 1
    if failed == 0:
      print("You win!")
      choice = input("Would you like to play again? (y/n)")
      if "y" in choice:
        run()
      elif "n" in choice:
        sys.exit()
      else:
        print("Something went wrong, type y or n.")
    guess = input("Guess a character:")
    guesses += guess
    if guess not in word:
      turns -= 1
      print("Wrong!")
      print(f"You have {turns} more guesses.")
      if turns == 0:
        print("Sorry, you lose!")
        choice = input("Would you like to play again? (y/n)")
        if "y" in choice:
          run()
        elif "n" in choice:
          sys.exit()
        else:
          print("Something went wrong, type y or n.")
run()