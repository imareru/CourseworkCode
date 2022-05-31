from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="912368.Noris",
                              host="127.0.0.1",
                              port="5432",
                              database="telegram_bot")
cursor = connection.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")

available_subject_names = ["Биологические науки", "Искусствоведение", "Исторические науки и археология",
                           "Культурология", "Медицинские науки", "Мультидисциплинарный раздел", "Науки о Земле",
                           "Педагогические науки", "Политология", "Психологические науки", "Сельскохозяйственные науки",
                           "Социологические науки", "Технические науки", "Физико-математические науки",
                           "Филологические науки", "Философские науки", "Химические науки", "Экономические науки",
                           "Юридические науки"]


# Класс для хранения состояний
class ChooseSubject(StatesGroup):
    waiting_for_subject_name = State()


# Обработчик первого шага
async def subject_choice(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_subject_names:
        keyboard.add(name)
    await message.answer("Выберите интересующую вас область исследования:", reply_markup=keyboard)
    await ChooseSubject.waiting_for_subject_name.set()


# Обработчик выбора предмета
async def selected_subject(message: types.Message, state: FSMContext):
    if message.text not in available_subject_names:
        await message.answer("Введите тему со встроенного меню.")
        return
    await state.update_data(chosen_subject=message.text.lower())

    postgre_query = "SELECT event_name, event_link, arranger FROM events WHERE events.subject LIKE %s"
    args = [message.text + '%']
    cursor.execute(postgre_query, args)
    records = cursor.fetchall()
    for one in records:

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Подробнее", url=one[1])
        button2 = types.InlineKeyboardButton("Организаторы", url=one[2])
        markup.add(button1, button2)
        await message.answer(one[0], reply_markup=markup)

    return


# Регистрация состояний в диспетчер
def register_handlers_subjects(dp: Dispatcher):
    dp.register_message_handler(subject_choice, commands="subject", state="*")
    dp.register_message_handler(selected_subject, state=ChooseSubject.waiting_for_subject_name)
