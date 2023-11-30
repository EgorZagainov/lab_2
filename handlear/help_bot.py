from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_help = Router()

@router_help.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Команды помощи"
        "\n"
        "start - запуск бота"
        "\n"
        "inline - Инлайн кнопки"
        "\n"
        "core - сколько ядер в процессоре "
    )
