from aiogram import Router
from aiogram.filters import Command
from aiogram.utils.markdown import hbold
from aiogram import types
from aiogram.types import Message




router_start = Router()

@router_start.message(Command("start"))
async def cmd_start(message: Message) -> None:
    kb = [
        [types.KeyboardButton(text='Я программист'),
         types.KeyboardButton(text='Я человек')],
        [types.KeyboardButton(text='Я не знаю кто я')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)

    await message.answer(f'Hello ,{hbold(message.from_user.full_name)}', reply_markup=keyboard)
