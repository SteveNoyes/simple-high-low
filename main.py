import random

def main():

  print("Welcome to the High-Low Game")
  print("--------------------------------")

  num_rounds = int(input("Please select how many rounds you would like to play. "))

  for i in range(num_rounds):
    # generate random numbers for player and computer, each round
    computer_random_number = random.randint(1, 100)
    player_random_number = random.randint(1, 100)

    # display user's number
    print("Your number is", player_random_number)

    # ask user to choose if their number is higher or lower than the computer's
    player_guess = input("Do you think your number is higher or lower than the computer's? ")

    print("The computer's number is", computer_random_number)
    print("Your number is", player_random_number)
    print(player_guess)

    # player wins if they guess correctly

    if(player_random_number < computer_random_number):
      print("winner")



if __name__ == "__main__":
  main()