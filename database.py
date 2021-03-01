import sqlite3
import json

def get_rating():
    con = sqlite3.connect("rating.db")
    cur = con.cursor()

    with open('rating.json') as rating_f:
            rating = json.load(rating_f)
    
    result = list(cur.execute(f"""SELECT name, score FROM rating""").fetchall())

    for n_id in rating:
        result[int(n_id)] = (result[int(n_id)][0], result[int(n_id)][1], rating[n_id])

    con.close()
    return result

def new_account(name):
    con = sqlite3.connect("rating.db")
    cur = con.cursor()
    if (None, None, []) in get_rating():
        n_id = get_rating().index((None, None, []))
        
        cur.execute(f"""UPDATE rating SET name = '{name}', score = {0} WHERE id = {n_id}""").fetchall()
  
        with open('rating.json') as rating_f:
            rating = json.load(rating_f)

        rating[str(n_id)] = [0, 0, 0, 0, 0, 0, 0, 0]

        with open('rating.json', 'w') as f:
            json.dump(rating, f)

    con.commit()
    con.close()


def update(level_n, score, id_n, result):
    with open('rating.json') as rating_f:
            rating = json.load(rating_f)

    rating[str(id_n)][level_n - 1] = result

    with open('rating.json', 'w') as f:
        json.dump(rating, f)
    
    con = sqlite3.connect("rating.db")
    cur = con.cursor()
    
    old_score = cur.execute(f"SELECT score FROM rating WHERE id = {id_n}").fetchall()
    print(old_score)
    cur.execute(f"""UPDATE rating SET score = {old_score[0][0] + score} WHERE id = {id_n}""").fetchall()

    con.commit()
    con.close()

data = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}