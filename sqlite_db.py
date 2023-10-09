import sqlite3 as sq


async def db_start():
    global db
    global cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, grup TEXT, half TEXT, ring TEXT, frm TEXT)")

    db.commit()


async def create_profile(user_id):
    user = cur.execute(
        "SELECT 1 FROM profile WHERE user_id == '{key}'".format(
            key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES( ?, ?, ?, ?, ?)",
                    (user_id, '', '', '', ''))
        db.commit()


async def update_frm(user_id, frm):
    cur.execute(
        "UPDATE profile SET frm = '{}' WHERE user_id == '{}'".format(frm, user_id))
    db.commit()


async def update_grup(user_id, grup):
    cur.execute(
        "UPDATE profile SET grup = '{}' WHERE user_id == '{}'".format(grup, user_id))
    db.commit()


async def update_half(user_id, half):
    cur.execute(
        "UPDATE profile SET half = '{}' WHERE user_id == '{}'".format(half, user_id))
    db.commit()


async def update_ring(user_id, ring):
    cur.execute(
        "UPDATE profile SET ring = '{}' WHERE user_id == '{}'".format(ring, user_id))
    db.commit()


async def show_db(user_id):
    data_students = cur.execute(
        "SELECT * FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()

    return data_students


async def show_all():
    data_students = """SELECT * FROM profile"""
    cur.execute(data_students)
    records = cur.fetchall()

    return records
