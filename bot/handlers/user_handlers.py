import sqlite3
from aiogram.filters import Command
from aiogram import Router, types

user_router = Router()
def openSQL():
    conn = sqlite3.connect('dice.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Data (UserID TEXT PRIMARY KEY, Username TEXT, Win777Count INTEGER DEFAULT 0, WinBarCount INTEGER DEFAULT 0, WinLemonCount INTEGER DEFAULT 0, WinGrapesCount INTEGER DEFAULT 0, AllWins INTEGER DEFAULT 0, SpinsCount INTEGER DEFAULT 0)')
    return conn, cur
@user_router.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    """Processes the `start` command."""
    conn, cur = openSQL()
    cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)',(msg.from_user.id, '@' + msg.from_user.username))
    conn.commit()
    conn.close()
    await msg.reply(f'Привет <b>{msg.from_user.first_name}</b>!')

@user_router.message(Command('help'))
async def cmd_help(msg: types.Message) -> None:
    """Processes the `help` command."""
    conn, cur = openSQL()
    cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)',(msg.from_user.id, '@' + msg.from_user.username))
    conn.commit()
    conn.close()
    await msg.reply('Мои команды:\n1. /start - запуск бота(приветствие)\n2. /me - твоя личная статистика\n3. /top - топ-5 лидеров беседы по выбитым 777')

@user_router.message(Command('me'))
async def cmd_me(msg: types.Message) -> None:
    conn, cur = openSQL()
    cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)',(msg.from_user.id, '@' + msg.from_user.username))
    conn.commit()
    cur.execute('SELECT Win777Count, WinBarCount, WinLemonCount, WinGrapesCount, AllWins, SpinsCount FROM Data WHERE UserID = ?', (msg.from_user.id,))
    fetch_list = cur.fetchone()
    conn.close()
    wins_777 = fetch_list[0]
    wins_bar = fetch_list[1]
    wins_lemon = fetch_list[2]
    wins_grapes = fetch_list[3]
    wins_all = fetch_list[4]
    spins = fetch_list[5]
    await msg.reply(f"<b>@{msg.from_user.username}</b>, вот твоя статистика:\n \
- Выбитых <i>777</i>: {wins_777}\n \
- Выбитых <i>BAR</i>: {wins_bar}\n \
- Выбитых <i>Лимончиков</i>: {wins_lemon}\n \
- Выбитых <i>Виноградиков</i>: {wins_grapes}\n \
- Всего <i>выигрышных прокрутов</i>: {wins_all}\n \
- Всего <i>прокрутов</i>: {spins}\n \
- Твой <i>процент выигрышного прокрута</i>: {wins_all / spins * 100:.2f}%")

@user_router.message(Command('top'))
async def cmd_top(msg: types.Message) -> None:
    conn, cur = openSQL()
    cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)',(msg.from_user.id, '@' + msg.from_user.username))
    conn.commit()
    conn.close()
    await msg.reply('В разработке...')

@user_router.message()
async def msg_user(msg: types.Message) -> None:
    if msg.content_type == 'dice' and msg.dice.emoji == '🎰':
        conn, cur = openSQL()
        cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)', (msg.from_user.id, '@' + msg.from_user.username))
        cur.execute('UPDATE Data SET SpinsCount = SpinsCount + 1 WHERE UserID = ?', (msg.from_user.id,))
        conn.commit()
        conn.close()
        if msg.dice.value == 64:
            conn, cur = openSQL()
            cur.execute('UPDATE Data SET Win777Count = Win777Count + 1 WHERE UserID = ?', (msg.from_user.id,))
            cur.execute('UPDATE Data SET AllWins = AllWins + 1 WHERE UserID = ?', (msg.from_user.id,))
            conn.commit()
            conn.close()
            await msg.reply(f'СЮДА! ПЛЮС <i>777</i> У <b>@{msg.from_user.username}</b>')
        elif msg.dice.value == 1:
            conn, cur = openSQL()
            cur.execute('UPDATE Data SET WinBarCount = WinBarCount + 1 WHERE UserID = ?', (msg.from_user.id,))
            cur.execute('UPDATE Data SET AllWins = AllWins + 1 WHERE UserID = ?', (msg.from_user.id,))
            conn.commit()
            conn.close()
            await msg.reply(f'Плюс <i>BAR</i> у <b>@{msg.from_user.username}</b>')
        elif msg.dice.value == 22:
            conn, cur = openSQL()
            cur.execute('UPDATE Data SET WinGrapesCount = WinGrapesCount + 1 WHERE UserID = ?', (msg.from_user.id,))
            cur.execute('UPDATE Data SET AllWins = AllWins + 1 WHERE UserID = ?', (msg.from_user.id,))
            conn.commit()
            conn.close()
            await msg.reply(f'Плюс <i>ВИНОГРАДИК</i> у <b>@{msg.from_user.username}</b>')
        elif msg.dice.value == 43:
            conn, cur = openSQL()
            cur.execute('UPDATE Data SET WinLemonCount = WinLemonCount + 1 WHERE UserID = ?', (msg.from_user.id,))
            cur.execute('UPDATE Data SET AllWins = AllWins + 1 WHERE UserID = ?', (msg.from_user.id,))
            conn.commit()
            conn.close()
            await msg.reply(f'Плюс <i>ЛИМОНЧИК</i> у <b>@{msg.from_user.username}</b>')
    elif msg.text:
        conn, cur = openSQL()
        cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)',(msg.from_user.id, '@' + msg.from_user.username))
        conn.commit()
        conn.close()