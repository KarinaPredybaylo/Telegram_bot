from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from tel_bot.trade_site import main

bot = Bot('5808472131:AAGNua_bgRWtHeG9FVEIWAqX-Og_ttmp3OQ')
dp = Dispatcher(bot)


def check_pair(text: str):
    return text.upper().replace(' ', '')


@dp.message_handler(commands=['start'])
async def start(message):
    mess = f'Hello, {message.from_user.first_name},  please choose a button!'
    markup_chat = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    site_button = KeyboardButton('Use site')
    chat_button = KeyboardButton('Use chatbot')
    markup_chat.add(site_button, chat_button)
    await message.answer(mess, reply_markup=markup_chat)


@dp.message_handler()
async def get_text(message):
    if message.text == 'Use chatbot':
        await message.answer(f'Please, write trade pair')
    elif message.text == 'Use site':
        markup_site = InlineKeyboardMarkup(row_width=1)
        site_button = InlineKeyboardButton('Use site', url='https://paper-trader.frwd.one/')
        markup_site.add(site_button)
        await message.answer('Please, click on the button', reply_markup=markup_site)
    else:
        if await main(check_pair(message.text)) == 'Error':
            await message.answer('Please, enter correct data')
        else:
            photo = open('image.jpg', "rb")
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=photo)


executor.start_polling(dp)
