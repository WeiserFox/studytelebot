from aiogram import Bot, Dispatcher, types
from cfg import TOKEN
import asyncio
import random

proxy_url = 'http://proxy.server:3128'

bot = Bot(token=TOKEN, proxy=proxy_url)

dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def hello(message):
    await message.answer("Привет! Напиши /help")

@dp.message_handler(commands="help")
async def help(message):
    await message.reply("Доступные команды:\n/random - выводит случайное число от 1 до 10\n/help - список команд")

@dp.message_handler(commands="random")
async def rand(message):
    await message.reply(f"Выпало {random.randint(1, 10)}")

@dp.message_handler(commands="lunch")
async def cmd_lunch(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="С макарошками")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

#@dp.message_handler()
#async def nocommand(message):
#    await message.reply("Неверная команда! Напишите /help")






async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
