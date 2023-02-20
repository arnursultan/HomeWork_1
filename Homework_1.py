from aiogram import Bot, Dispatcher, types, executor
import config
from random import randint
bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}.")
    await message.answer(f"Use /gametart to start the game.")

@dp.message_handler(commands="gamestart")
async def game(message:types.Message):
    await message.answer("Let's start the game!")
    await message.answer("Enter any number from 1 to 3.")

@dp.message_handler(regexp=r"^[1-3]")
async def randomsz(message:types.Message):
    integ = randint(1, 3)
    user_int = int(message.text)
    if integ == user_int:
        await message.reply("Congratulations! You guessed right!")
    else:
        await message.reply("You lost!")

executor.start_polling(dp)