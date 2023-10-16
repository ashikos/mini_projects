
import random
min_value = 1
max_value = 6

def get_dice_value():
    value = random.randint(min_value, max_value)
    return value


while True:
    players = input("Please enter number of players (1-4) :  ")
    if players.isdigit() :
        players = int(players)
        if  1 < players <= 4:
            break
        else:
            print("There must be atleast 2 or max 4 players to start the game")
    else:
        print("Enter a valid number")

total_score = [0 for _ in range(players)]


while max(total_score) <30:

    for index, player in enumerate(total_score):
        score = 0
        while True:
            die = input(f"would you like to role the die  player {index+1} (y/n): ")
            if die.lower() == 'y':
                dice = get_dice_value()
                print("Dice value is : ", dice)
                if dice != 1:
                    score = score + dice
                    print("Current score is : ", score)
                else:
                    total_score[index] = 0
                    print("Your tun is over")
                    break
            else:
                total_score[index] = total_score[index] + score
                print("Your score is: ", total_score[index])
                print(total_score)
                break

winner = total_score.index(max(total_score))
print(f"Winner is player_{winner+1}")
        
