import random

best_score = None
playing = True

while playing:
  while True:
    try:
      a = int(input("Enter a start number: "))
      b = int(input("Enter an end number: "))
      if a <= b:
        break
      print("The start number must be less than or equal to the end number.")
    except ValueError:
      print("Please enter valid whole numbers.")

  while True:
    try:
      max_attempts = int(input("How many attempts would you like? "))
      if max_attempts > 0:
        break
      print("Please enter a positive number of attempts.")
    except ValueError:
      print("Please enter a valid whole number.")

  number_to_guess = random.randint(a, b)
  attempts = max_attempts

  while attempts > 0:
    try:
      guess = int(input(f"Guess the number between {a} and {b}: "))

      if guess < number_to_guess:
        attempts -= 1
        print(f"Too low! You have {attempts} attempts left.")
      elif guess > number_to_guess:
        attempts -= 1
        print(f"Too high! You have {attempts} attempts left.")
      else:
        print(f"Congratulations! You guessed the number. The number was {number_to_guess}, and you had {attempts} attempts left.")
        score = max_attempts - attempts
        if best_score is None or score < best_score:
          best_score = score
          print(f"New best score: {best_score} attempts.")
        else:
          print(f"Your score was {score} attempts. Your best score is {best_score} attempts.")
        break
    except ValueError:
      print("Please enter a valid number.")

  if attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

  while True:
    choice = input("Would you like to continue playing? (yes/no): ").lower()
    if choice in ("yes", "y"):
      break
    if choice in ("no", "n"):
      if best_score is not None:
        print(f"Your best score this session was {best_score} attempts.")
      print("Thanks for playing!")
      playing = False
      break
    print("Please enter yes or no.")
