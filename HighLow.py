import random
import SQLIfy
import Main as M

# cr = M.cur

def score(res):
    if res == 0:
        return 5000
    elif res == 1:
        return 1000
    elif res == 2:
        return 500
    else:
        return 0

def msg(c,rand_num):
    if c == 0:
        return "HOLY HECK YOU GUESSED IT, THE NUMBER WAS {num}".format(num=rand_num)
    elif c == 1:
        return "Close enough!\nthe number was {n}".format(n=rand_num)
    elif c == 2:
        return "Nope, missed by a long shot!\nthe number was {n}".format(n=rand_num)
    else:
        return ""

def hl(rand): # the game itself
    print(rand)
    try: #handling mismatch
        num = int(input())
        diff = abs(rand - num)
        if diff == 0:
            return 0
        elif diff <= 10:
            return 1
        elif diff > 10:
            return 2
    except:
        return 3


def show_leaderboard(name):
    # sql queries here
    inleaderboard=True
    while inleaderboard:
        print("leaderboard with "+name)
        SQLIfy.select_from_leaderboards(name)
        lstatus = input("Input q to quit: ")

        if lstatus == 'q':
            inleaderboard = False

def add_score(score,name):
    #SQLIfy.insert_to_user(0,name)
    SQLIfy.insert_to_user(score,name)

def playHL(name):
    finished = False
    while not finished:
        RAND_NUM = random.randint(1,100) #result
        print("Guess a number between 1-100")
        result=hl(RAND_NUM)
        if result == 3:
            print("input type mismatch, score not added")
        print(msg(result,RAND_NUM))
        print("adding score...")
        player_score = score(result)
        add_score(player_score,name)
        print("score added")
        print("continue? Y/N")
        c = input()
        if c.lower() == "n":
            finished = True

def register_user(name):
    pass #execute sql queries

def fsm():
    print("Welcome to high low, the game!\n\n")
    done = False
    while not done:
        print("Enter your name!\ntype q to quit")
        name = input()

        if name == "q":
            print("Thanks for playing!")
            done = True
            break

        if len(name) < 3:
            print("the length of your name must be greater than or equal to 3")
            continue
        playing = True
        while playing:
            print("Welcome "+name+"!")
            print("Main menu\n1.Play\n2.Leaderboards\n3.Quit")
            choice = int(input())
            if choice == 1:
                playHL(name)
            elif choice == 2:
                show_leaderboard(name)
            elif choice == 3:
                playing = False

fsm()
