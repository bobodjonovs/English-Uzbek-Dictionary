"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from oxfordlookup import getDefinations
from googletrans import Translator

translator = Translator()

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5403150065:AAGFN-dzVNpV-3dJ36WjCH8xrict-pI07x0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

print(translator)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomualeykum!Botga xush kelibsiz. So`z yoki matn yuboring!")



@dp.message_handler(commands=['help'])
async def help_user(message: types.Message):
    """
    Bi funksiya helpni bosganda chaqiriladi
    """
    await message.answer("Qanday yordam bera olaman!")



@dp.message_handler()
async def tarjimon(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    lang = translator.detect(message.text).lang # hello
    if len(message.text.split()) > 2:

        dest = 'uz' if lang == 'en' else 'en'   
        await message.reply(translator.translate(message.text,dest).text)
    
    else:
        if lang == "en":
            word = message.text 
        else:

            word = translator.translate(message.text, dest='en').text
        
        look_up = getDefinations(word)

        if look_up:
            await message.reply(f"Word: {word}, definition: None")    
            await message.reply_voice(look_up)
                                
        await message.reply("Not have ")
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


