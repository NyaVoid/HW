import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData

API_TOKEN = 'token'

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
    keyboard.add(button_calculate, button_info)
    await message.reply("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(Text(equals='Рассчитать', ignore_case=True), state='*')
async def main_menu(message: types.Message):
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
    inline_keyboard.add(button_calories, button_formulas)
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161\n"
        "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5"
    )
    await bot.send_message(call.message.chat.id, formula_text)

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    age = data['age']
    growth = data['growth']
    weight = data['weight']

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.reply(f"Ваша норма калорий: {calories:.2f} ккал в день.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
