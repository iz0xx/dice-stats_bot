from gc import callbacks

import aiogram
from aiogram.types import InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram import types

builder = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='FUN', web_app=WebAppInfo(url='https://m.vk.com/rgnabarskayamylove')),]])