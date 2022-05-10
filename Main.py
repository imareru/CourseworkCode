import asyncio

import keyboard as keyboard
from aiogram.types import BotCommand
from steps import register_handlers_subjects
from common import register_handlers_common
import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logger = logging.getLogger(__name__)
# Объект бота
bot = Bot(config.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())
# Включаем логирование, чтобы не пропустить важные сообщения
#logging.basicConfig(level=logging.INFO)


# @dp.message_handler(commands=['start'])
# async def start_message(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Вперед", callback_data="answers"))
#     await message.answer("Бот приветствует вас. Пройдем небольшой тест?", reply_markup=keyboard)


# @dp.callback_query_handler(text="answers")
# async def send_test_results(call: types.CallbackQuery):
#     await call.message.answer("Принято")
#

# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/subject", description="Выбрать тему"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")


    # Регистрация хэндлеров
    register_handlers_subjects(dp)
    register_handlers_common(dp)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()

# RUN
# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)
#
if __name__ == '__main__':
    asyncio.run(main())
