from random import randint
from aiogram import Router, F
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command


router_random = Router()


@router_random.message(Command("random"))
async def random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="НАЖМИ НА МЕНЯ", callback_data="random_vale_number")
    )
    await message.answer(
        "Нажми на меня для вывода" "\n" " рандомного числа", reply_markup=builder.as_markup()
    )


@router_random.callback_query(F.data == "random_vale_number")
async def random_number(callback: types.CallbackQuery):
    await callback.message.send_copy(str(randint(1, 100)))
    await callback.answer()