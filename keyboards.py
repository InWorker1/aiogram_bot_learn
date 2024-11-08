from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main_R = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='каталог')],
#     [KeyboardButton(text='корзина'), KeyboardButton(text='контакты')]
# ],          resize_keyboard=True, input_field_placeholder='pick something')             
# ----- создана клавиатура, в которой три кнопки. одна сверху и две снизу. ( Reply Buttons )
# ----- 3 аргумента. первый отвечает за саму клавиатуру. второй за размер ( сводит размер к минимуму, так красивее) и 3 арг добавляет надпись к пользовательской клавиатуре

main_I = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='my soundcloud', url='https://on.soundcloud.com/QcpGxm6GtvpDvPfE6')]])

main_K = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='какие выпустились треки?', callback_data='give_how_much_traks')]])

troll = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='show your traks', callback_data='troll')]])    # для прикола

# cars = ['shine', 'emptiness', 'cheer up']                   # ----- пример, если названия меняются, а переписывать код не хочется. клавиатуру можно сделать настраиваемой под базу данных.                          
# async def reply_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(2).as_markup()           # ----- сколько кнопок в ряду и констант
# # await msg.answer('hi', reply_markup=await inline_cars()) ----- то что нужно писать для вывода подстраиваемой клавиатуры
# cars = ['shine', 'emptiness', 'cheer up']                   # ----- пример, если названия меняются, а переписывать код не хочется. клавиатуру можно сделать настраиваемой под базу данных.                          
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, url='https://car.ru'))
#     return keyboard.adjust(2).as_markup() 
# # ----- то же самое, только Inline кнопки
