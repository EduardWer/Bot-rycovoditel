from aiogram import Bot,types,executor
from aiogram.dispatcher import Dispatcher

token = ""

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def Start(message:types.Message):
    pass







executor.start_polling(dp,skip_updates=True)