import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text 
from crud_functions import initiate_db, get_all_products

API_TOKEN = 'token'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

initiate_db()

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
    products = get_all_products()

    if not products:
        await message.reply("Нет доступных продуктов.")
        return

    for product in products:
        title, description, price = product
        await message.reply(
            f'Название: {title} | Описание: {description} | Цена: {price}'
        )

    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    for product in products:
        title = product[0]
        button = InlineKeyboardButton(title, callback_data=f'product_buying_{title}')
        inline_keyboard.add(button)

    await message.reply("Выберите продукт для покупки:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data.startswith('product_buying_'))
async def send_confirm_message(call: types.CallbackQuery):
    product_name = call.data.split('_')[2]
    await bot.send_message(call.message.chat.id, f"Вы успешно приобрели продукт: {product_name}!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
