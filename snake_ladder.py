import random
import time

print('Snake & Ladder Game...!')

snakeAddress = {27: 5, 40: 3, 43: 18, 54: 31, 66: 45, 76: 58, 89: 53, 99: 41}
ladderAddress = {4: 25, 13: 46, 33: 49, 42: 63, 50: 69, 62: 81, 74: 92}


def ladder(data):
    if (data in ladderAddress.keys()):
        print("\033[1m" + "Ladder...!" + "\033[0m")
        return ladderAddress[data]
    else:
        return data


def snake(data):
    if (data in snakeAddress.keys()):
        print("\033[1m" + "Snake...!" + "\033[0m")
        return snakeAddress[data]
    else:
        return data


def game_end(data):
    return (data >= 100)

def game_start():
    player_name = "\033[1m" + "Ishanka" + "\033[0m"
    while (True):
        random_data = random.randint(1, 6)
        print("value of cube :", random_data)
        if (random_data == 1 or random_data == 6):
            game_process(player_name, random_data)
        else:
            print("\033[1m" + "try again..!" + "\033[0m")
        time.sleep(1)

def game_process(player_name_data, score_data):

    player_name = player_name_data
    score = score_data

    while (True):

        print(player_name, "you are in :", score)

        time.sleep(1)
        random_data = random.randint(1, 6)
        print("value of cube :", random_data)

        score += random_data
        score = ladder(score)
        score = snake(score)

        if (game_end(score)):
            print(player_name, "You won the game..!")
            exit()

game_start()
