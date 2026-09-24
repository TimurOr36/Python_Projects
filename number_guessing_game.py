import random

a = int(input("Enter a start number: "))
b = int(input("Enter an end number: "))
number_to_guess = random.randint(a, b)

attempts = 10

while True:
  try:
    guess = int(input(f"Guess the number between {a} and {b}: "))
  
    if guess < number_to_guess:
      attempts -= 1
      print(f"Too low! You have {attempts} attempts left.")
    elif guess > number_to_guess:
      attempts -= 1
      print(f"Too high! You have {attempts} attempts left.")
    elif attempts <= 0 and guess != number_to_guess:
      print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
      break
    else:
      print(f"Congratulations! You guessed the number. The number was {number_to_guess}, and you had {attempts} attempts left.")
      best_score = None
      if best_score is None or attempts < best_score:
        best_score = attempts
        print(f"You unlocked a new best score: You guessed the number in {10 - best_score} attempts.")
      break
  except ValueError:
    print("Please enter a valid number.")
