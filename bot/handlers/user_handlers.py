import sqlite3
from aiogram.filters import Command
from aiogram import Router, types

user_router = Router()
def openSQL():
    conn = sqlite3.connect('dice.db')
    cur = conn.cursor()
    return conn, cur
# @user_router.message(Command('start'))
# async def cmd_start(msg: types.Message) -> None:
#     """Processes the `start` command."""
#     await msg.answer('<b>Привет</b>!')

@user_router.message(Command('help'))
async def cmd_help(msg: types.Message) -> None:
    """Processes the `help` command."""
    await msg.answer("в разработке...\n")

@user_router.message(Command('me'))
async def cmd_me(msg: types.Message) -> None:
    conn, cur = openSQL()
    cur.execute('SELECT WinCount FROM Data WHERE UserID = ?', (msg.from_user.id,))
    wins = cur.fetchone()[0]
    await msg.answer(f"<b>{msg.from_user.first_name}</b>, у тебя <u>{wins}</u> выбитых 777!")

@user_router.message()
async def msg_user(msg: types.Message) -> None:
    if msg.content_type == 'dice' and msg.dice.emoji == '🎰':
        conn, cur = openSQL()
        cur.execute('INSERT OR IGNORE INTO Data (UserID, Username) VALUES (?, ?)', (msg.from_user.id, '@' + msg.from_user.username))
        conn.commit()
        conn.close()

        if msg.dice.value == 64:
            conn, cur = openSQL()
            cur.execute('SELECT UserID, WinCount FROM Data WHERE UserID = ?', (msg.from_user.id,))
            fetch_list = list(cur.fetchone())
            win_count = fetch_list[1] if fetch_list[1] is not None else 0
            win_count += 1
            cur.execute('UPDATE Data SET WinCount = ? WHERE UserID = ?', (win_count, msg.from_user.id))
            conn.commit()
            conn.close()
            await msg.reply(f'СЮДА! ПЛЮС ОДНА В КОПИЛОЧКУ У <b>@{msg.from_user.username}</b>')



