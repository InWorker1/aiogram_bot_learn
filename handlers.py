from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
import config as conf

router = Router()               # ----- тот же dp - despetcher

# @router.message(CommandStart())
# async def start(msg: Message):
#     await msg.answer('hi my name von', reply_markup=kb.troll)


# @router.callback_query(F.data == 'troll')
# async def troll_inline(cb: CallbackQuery):
#     await cb.answer('прочитал - сосал', show_alert=True)
#     await cb.message.answer('попался лошок перекаченный')
@router.message(CommandStart())             # ---- команда старта 
async def cmd_start(msg: Message):
    await msg.answer('hi! my name is von. i am music producer', reply_markup=kb.main_K)             # ----- inline кнопки
    await msg.answer_photo(photo='AgACAgIAAxkBAAMuZy0bETXMO67UHV0Fy6cZ4U5iZNcAAsfnMRtg2HBJ3Am7vZLQFbkBAAMCAANtAAM2BA', caption='', reply_markup=kb.main_I)        # ---- команда, чтобы бот отрпавил фото (caption= - это текст, который будет вместе с фото отправлен)
                        # ----- команда reply_markup=kb.main_k, добавляет к сообщению бота клавиатуру с reply или inline кнопками. ( клавиатура импортирована из файла keyboars с сокрщ названием -- kb )
                        

@router.message(Command('ahelp'))           # ----- пример команды 
async def get_help(msg: Message):
    await msg.answer('в этом телеграмм боте вы можете: ')


@router.message(F.text.lower().strip() == 'как дела?') # ---- ответ на текстовое сообещение
async def how_are_u(msg: Message):
    await msg.answer('все в порядке!)')


@router.message(F.photo)                    # ----- работа в фото 
async def get_photo(msg: Message):
    await msg.answer(f'ID photo: {msg.photo[-1].file_id}')              # ----- индекс минус один, потому что это лучшее качество фото в телеграмме




@router.message(Command('getID'))            # ----- команда дающая айди и имя пользователя, который ее использовал
async def get_ID(msg: Message):
    await msg.reply(f'your ID: {msg.from_user.id}\nyour name: {msg.from_user.first_name}') # ---- так же можно доаставать куча инфы с from_user 
                                                                                           # ----- reply делает так, что бот ОТВЕЧАЕТ на твое сообщение с командой

@router.callback_query(F.data == 'give_how_much_traks')                 # ------ callback действие после нажатие кнопки с индексом (callbackом) - give_how_much_tracks
async def give_how_much_traks(cb: CallbackQuery):
    tt = ''
    for el in conf.tracks:
        tt += el
        tt += ',\n'
    await cb.answer('на нахуй')             # ----- короткое уведомление о выполнении callback для питона и для пользователя бота))) 
    # await cb.answer('сосал?', show_alert=True) # ----- отдельное окно с мини подтверждением действий. можно использовать для проверок подписки или оплаты!
    await cb.message.answer(f'this is my tracks: {tt}')
