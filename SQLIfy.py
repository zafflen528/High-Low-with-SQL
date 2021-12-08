from Main import cur
from Main import mariadb

def leaderboard_queries(name:str):
    other_users= "SELECT * FROM user  GROUP BY score desc LIMIT 5;"
    user_score = "SELECT * FROM user WHERE username=?"

    cur.execute(other_users)
    for (username,score) in cur:
        print(username +" " + str(score))

    print()
    cur.execute(user_score,(name,))
    for (username,score) in cur:
        print(username +" " + str(score))


def select_from_leaderboards(curr_user:str):
    leaderboard_queries(curr_user)


def user_exist(name:str):
    determine_user_exist = "SELECT * FROM user where username=?"
    cur.execute(determine_user_exist,(name,))
    for (user) in cur:
        return True
    return False

def insert_to_user(score:int,name:str):
    existing_user_query = "UPDATE user SET score=score+? WHERE username=?"
    new_user_query = "INSERT INTO user(username, score) VALUES(?,?)"

    if user_exist(name):
        cur.execute(existing_user_query,(score,name))
        print("+"+str(score) +" to "+name)
    else:
        cur.execute(new_user_query,(name,score))
        print("New user detected!\n+"+str(score)+" to "+name)
