from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, Bot, F



router_inline = Router()
@router_inline.message(Command("inline_game"))
async def cmd_inline_url(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Камень", callback_data='stone')
        )
    builder.row(types.InlineKeyboardButton(
        text="Ножницы",callback_data='scissors')
        )
    builder.row(types.InlineKeyboardButton(
        text="Бумага", callback_data='paper')
    )
    await message.answer(
        'Камень ножницы бумага', reply_markup=builder.as_markup(),
    )



@router_inline.callback_query(F.data == 'stone')
async def cmd_stone(callback: types.CallbackQuery):
    await callback.message.answer('Камень бьёт ножницы')
    await callback.answer()

@router_inline.callback_query(F.data == 'scissors')
async def cmd_scissors(callback: types.CallbackQuery):
    await callback.message.answer('ножницы бьют бумагу')
    await callback.answer()


@router_inline.callback_query(F.data == 'paper')
async def cmd_paper(callback: types.CallbackQuery):
    await callback.message.answer('бумагу бьёт камень')
    await callback.answer()


