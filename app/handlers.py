from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command


import app.keyboards as kb

router=Router()


@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Привет!',reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('Вы нажали на кнпоку помощи')

@router.message(F.text=='Каталог')
async def nice(message:Message):
    await message.answer('Выберите категорию товара',reply_markup=kb.catalog)

@router.callback_query(F.data=='t-shirt')
async def t_shirt(callback:CallbackQuery):
    await callback.answer('Вы Выбрали категорию футболок')





@router.callback_query(F.data=='da')
async def t_shirt(callback:CallbackQuery):
    await callback.answer('ША')