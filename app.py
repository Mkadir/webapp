from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Start Learning",
reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Learning",
web_app=WebAppInfo(url="https://learning.mkadir.me/"))))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
