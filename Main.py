import asyncio
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


# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/subject", description="Выбрать тему"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


async def main():
    # Настройка логирования
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
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
