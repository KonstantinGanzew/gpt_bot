import sqlite3 as sq

# Создание бд
async def db_start():
    db = sq.connect(r'.\bd\base\\user_data.db')
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user_data(
        user_id INTEGER PRIMARY KEY,
        last_mileage INTEGER,
        message TEXT)
        ''')
    db.commit()

async def create_profile(user_id):
    with sq.connect(r'.\bd\base\\user_data.db') as con:
        cur = con.cursor()
        user = cur.execute(f"SELECT 1 FROM user_data WHERE user_id == '{int(user_id)}'").fetchone()
        if not user:
            cur.execute('INSERT INTO user_data VALUES(?, ?, ?)', (int(user_id), 0, ''))
        return cur.fetchall()

# Установить пробег
async def set_mileage(user_id, mileage):
    with sq.connect(r'.\bd\base\\user_data.db') as con:
        cur = con.cursor()
        cur.execute(f'UPDATE user_data SET last_mileage={int(mileage)} WHERE user_id={int(user_id)}')
        return cur.fetchall()

# Получить полбег
async def get_mileage(user_id):
    with sq.connect(r'.\bd\base\\user_data.db') as con:
        cur = con.cursor()
        cur.execute(f'SELECT last_mileage FROM user_data WHERE user_id={int(user_id)}')
        return cur.fetchall()

