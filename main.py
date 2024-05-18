import random

def main():

  print("Welcome to the High-Low Game")
  print("--------------------------------")

  num_rounds = int(input("Please select how many rounds you would like to play. "))

  # counter to track wins
  player_track_record = 0


  for i in range(num_rounds):
    # generate random numbers for player and computer, each round
    computer_random_number = random.randint(1, 100)
    player_random_number = random.randint(1, 100)

    # display user's number
    print("Your number is", player_random_number)

    # ask user to choose if their number is higher or lower than the computer's
    player_guess = input("Do you think your number is higher or lower than the computer's? ")

    # check if player was correct by saying lower
    if(player_random_number < computer_random_number and player_guess == "lower"):
      print("You were right! The computer's number was", computer_random_number)
      # add win to track record
      player_track_record += 1
    # check if player was correct by saying higher
    elif(player_random_number > computer_random_number and player_guess == "higher"):
      print("You were right! The computer's number was", computer_random_number)
      # add win to track record
      player_track_record += 1
    # if the above two and false than the play did not win
    else:
      print("That's incorrect. The computer's number was", computer_random_number)

    # at the end of each round print out track record, and new line
    print("Your score is now", player_track_record, "\n")

if __name__ == "__main__":
  main()