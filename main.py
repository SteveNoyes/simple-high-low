import random

def main():

  print("Welcome to the High-Low Game")
  print("--------------------------------")

  num_rounds = int(input("Please select how many rounds you would like to play. "))

  for i in range(num_rounds):
    # generate random numbers for player and computer, each round
    computer_random_number = random.randint(1, 100)
    player_random_number = random.randint(1, 100)

    print("The computer's number is", computer_random_number)
    print("Your number is", player_random_number)


if __name__ == "__main__":
  main()