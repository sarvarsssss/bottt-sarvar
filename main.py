import logging

from aiogram import Bot, Dispatcher, executor, types
from oxfordlookup import getDefinitions
from googletrans import Translator
translator = Translator()
API_TOKEN = '1996844144:AAHw4RCN2TdizLsBhDfpjv_9Mnb_OtOmQl4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nThis is english translator bot \nCreated by sarvarsssss 😎")
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Do you need Help!\n Just call me \nWhenever you lonely 😊")

@dp.message_handler()
async def tarjimon(message: types.Message):
    print(message)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)