import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router


bot = Bot(token=TOKEN)                  # ----- токен бота ( пиздец удивительно )
dp = Dispatcher()                       # ----- диспетчер бота ( все что выполняется, выполняется через эту суку )


async def main():       # ---- старт бота ( дефолт )
    dp.include_router(router)       # ----- для того чтобы питон понимал, что роутер это диспетчер. 
    await dp.start_polling(bot) 

if __name__ == '__main__':      # ----- всегда писать тоже дефолт ( такой же старт )
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
