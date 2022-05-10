from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

available_subject_names = ["Информационные технологии", "Естественные науки", "Филология", "Юриспруденция"]


class ChooseSubject(StatesGroup):
    waiting_for_subject_name = State()


async def subject_choice(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_subject_names:
        keyboard.add(name)
    await message.answer("Выберите интересующую вас область:", reply_markup=keyboard)
    await ChooseSubject.waiting_for_subject_name.set()


async def selected_subject(message: types.Message, state: FSMContext):
    buttons = [
        types.InlineKeyboardButton(text="Подробнее", url="https://schoolstars.ru/"),
        types.InlineKeyboardButton(text="Контакты", url="https://schoolstars.ru/science-knowledge-2021-2022/")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    if message.text.lower() not in available_subject_names:
        # await message.answer("Пожалуйста, выберите область, используя клавиатуру ниже.")
        await message.answer("III Международная on-line конференция “Science knowledge 2021/2022”, 10.09.2021-31.08.2022", reply_markup=keyboard)
        return
    # await state.update_data(selected_subject=message.text.lower())
    #
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # # for size in available_food_sizes:
    # #     keyboard.add(size)
    # # # Для последовательных шагов можно не указывать название состояния, обходясь next()
    # await ChooseSubject.next()
    # await message.answer("Теперь выберите размер порции:", reply_markup=keyboard)


def register_handlers_subjects(dp: Dispatcher):
    dp.register_message_handler(subject_choice, commands="subject", state="*")
    dp.register_message_handler(selected_subject, state=ChooseSubject.waiting_for_subject_name)
