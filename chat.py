from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from keyboard import def get_function_keyboard


class Form(StatesGroup):
    first_number = State()

def calculator(dp: Dispatcher):
    @dp.message(Command('start'))
    async def cmd_start(message: types.Message, state: FSMContext):
        await state.set_state(Form.primer)
        await message.answer("Здравствуйте, введите пример")

    @dp.message(Form.primer)
    async def process_primer(message: types.Message, state: FSMContext):
        await state.update_data(primer=message.text)