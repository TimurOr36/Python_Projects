import random

count = 0
while True:
  choice = input("Roll the dice? (yes/no): ").lower()
  if choice == "yes":
    play = int(input("How many times would you like to roll the dice? "))
    for i in range(play):
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      count += 1
      print(f"You rolled a {die1} and a {die2}. Total result is {die1 + die2}. This is your {count} roll.")
  elif choice == "no":
    print(f"Thank you for playing! You rolled the dice {count} times.")
    break
  else:
    print("Invalid input. Please enter 'yes' or 'no'.")