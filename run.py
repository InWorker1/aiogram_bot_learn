import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
# from aiogram import CommandStart
from config import TOKEN

bot = Bot(token=TOKEN)                  # ----- токен бота ( пиздец удивительно )
dp = Dispatcher()                       # ----- диспетчер бота ( все что выполняется, выполняется через эту суку )


@dp.message(CommandStart())             # ---- команда старта 
async def cmd_start(msg: Message):
    await msg.answer('hi! my name is von. i am music producer')
    await msg.answer_photo(photo='AgACAgIAAxkBAAMuZy0bETXMO67UHV0Fy6cZ4U5iZNcAAsfnMRtg2HBJ3Am7vZLQFbkBAAMCAANtAAM2BA', caption='hi! my name is von. i am music producer')        # ---- команда, чтобы бот отрпавил фото (caption= - это текст, который будет вместе с фото отправлен)



@dp.message(Command('ahelp'))           # ----- пример команды 
async def get_help(msg: Message):
    await msg.answer('в этом телеграмм боте вы можете: ')


@dp.message(F.text.lower().strip() == 'как дела?') # ---- ответ на текстовое сообещение
async def how_are_u(msg: Message):
    await msg.answer('все в порядке!)')


@dp.message(F.photo)                    # ----- работа в фото 
async def get_photo(msg: Message):
    await msg.answer(f'ID photo: {msg.photo[-1].file_id}')              # ----- индекс минус один, потому что это лучшее качество фото в телеграмме


@dp.message(Command('getID'))            # ----- команда дающая айди и имя пользователя, который ее использовал
async def get_ID(msg: Message):
    await msg.reply(f'your ID: {msg.from_user.id}\nyour name: {msg.from_user.first_name}') # ---- так же можно доаставать куча инфы с from_user 
                                                                                           # ----- reply делает так, что бот ОТВЕЧАЕТ на твое сообщение с командой



async def main():       # ---- старт бота ( дефолт )
    await dp.start_polling(bot) 

if __name__ == '__main__':      # ----- всегда писать тоже дефолт ( такой же старт )
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
