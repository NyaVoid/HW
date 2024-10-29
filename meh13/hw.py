import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from crud_functions import initiate_db, get_all_products, add_user, is_included

API_TOKEN = 'token'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

initiate_db()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    button_buy = KeyboardButton('Купить')
    button_register = KeyboardButton('Регистрация')
    keyboard.add(button_calculate, button_info, button_buy, button_register)
    await message.reply("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(Text(equals='Регистрация', ignore_case=True))
async def sing_up(message: types.Message):
    await message.reply("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.reply("Пользователь существует, введите другое имя.")
        return
    
    await state.update_data(username=username)
    await message.reply("Введите свой email:")
    await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.reply("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    user_data = await state.get_data()
    username = user_data.get('username')
    email = user_data.get('email')
    add_user(username, email, age)
    await message.reply("Вы успешно зарегистрированы!")
    await state.finish()

@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: types.Message):
    products = get_all_products()
    if not products:
        await message.reply("Нет доступных продуктов.")
        return

    for product in products:
        title, description, price = product
        await message.reply(f'Название: {title} | Описание: {description} | Цена: {price}')

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
