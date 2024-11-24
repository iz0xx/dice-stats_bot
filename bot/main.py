import asyncio
from aiogram import  Dispatcher, types

from bot_instance import bot
from handlers.user_handlers import user_router

async def main() -> None:
    """The main function of the bot which will execute our event loop and start polling."""

    dp = Dispatcher()

    register_routers(dp)

    await dp.start_polling(bot)

def register_routers(dp: Dispatcher) -> None:
    """Register router"""

    dp.include_router(user_router)

if __name__ == '__main__':
    asyncio.run(main())