import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text 

API_TOKEN = '7325779591:AAHmV3s7ajJdM9QRTClMOrnE31XHUYX4B3M'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    button_buy = KeyboardButton('Купить')
    keyboard.add(button_calculate, button_info, button_buy)
    await message.reply("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Product1", "description": "описание 1", "price": 100},
        {"name": "Product2", "description": "описание 2", "price": 200},
        {"name": "Product3", "description": "описание 3", "price": 300},
        {"name": "Product4", "description": "описание 4", "price": 400},
    ]

    for product in products:
        await message.reply(
            f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}'
        )

    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    for product in products:
        button = InlineKeyboardButton(product["name"], callback_data='product_buying')
        inline_keyboard.add(button)

    await message.reply("Выберите продукт для покупки:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
