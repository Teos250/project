from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup)

main= ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                    [KeyboardButton(text='Корзина')],
                                    [KeyboardButton(text='Контакты'),
                                    KeyboardButton(text='Анас')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите пункт меню..'
                                
                                    )

catalog=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки',callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кроссовки',callback_data='shoes')],
    [InlineKeyboardButton(text='Кепки',callback_data='cap')],
    [InlineKeyboardButton(text='Да',callback_data='da')]
    ])