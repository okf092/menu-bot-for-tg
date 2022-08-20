from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

# I am made only 4 positions, if you need, create more...

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['McDonalds', 'Subway', 'Nestle', 'Крошка-Картошка']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Hello!\nThis bot creates data-files with restaurant menus\nPlease, choose category:',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals='McDonalds'))
async def start(message: types.Message):
    """sending McDonalds files"""
    await message.answer('Creating file...')
    await message.reply_document(open('data/48_Макдоналдс_(McDonalds).csv', 'rb'))
    await message.reply_document(open('data/48_Макдоналдс_(McDonalds).json', 'rb'))
    await message.answer('Done!')


@dp.message_handler(Text(equals='Subway'))
async def start(message: types.Message):
    """sending Subway files"""
    await message.answer('Creating file...')
    await message.reply_document(open('data/44_Subway.csv', 'rb'))
    await message.reply_document(open('data/44_Subway.json', 'rb'))
    await message.answer('Done!')


@dp.message_handler(Text(equals='Nestle'))
async def start(message: types.Message):
    """sending Netle files"""
    await message.answer('Creating file...')
    await message.reply_document(open('data/43_Nestle.csv', 'rb'))
    await message.reply_document(open('data/43_Nestle.json', 'rb'))
    await message.answer('Done!')


@dp.message_handler(Text(equals='Крошка-Картошка'))
async def start(message: types.Message):
    """sending Крошка-Картошка files"""
    await message.answer('Creating file...')
    await message.reply_document(open('data/47_Крошка_Картошка.csv', 'rb'))
    await message.reply_document(open('data/47_Крошка_Картошка.json', 'rb'))
    await message.answer('Done!')


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
