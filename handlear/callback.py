from aiogram import Router, F,types
from random import randint


router_callback = Router()


@router_callback.callback_query(F.data == "random_vale_number")
async def random_number(callback: types.CallbackQuery):
    await callback.message.send_copy(str(randint(1, 100)))
    await callback.answer()