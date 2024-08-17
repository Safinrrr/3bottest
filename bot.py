import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook

# Установите свой токен бота
BOT_TOKEN = '7354136013:AAEmvylGHcdVc0FVVa7fBvuV62d5f0qyRto'

# Настройки вебхука
WEBHOOK_HOST = 'http://qwer-6e1e47-d3796e-46-8-230-125.traefik.me/'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Настройки сервера
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 3000

async def start_bot(dispatcher: Dispatcher):
    # Установка вебхука
    await bot.set_webhook(WEBHOOK_URL)
    print(f'Webhook setup: {WEBHOOK_URL}')

async def stop_bot(dispatcher: Dispatcher):
    # Удаление вебхука
    await bot.delete_webhook()
    print('Webhook deleted')

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Вы сказали: {message.text}")

if __name__ == '__main__':
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)

    # Регистрация обработчиков
    dp.register_message_handler(echo)
    dp.register_on_startup(start_bot)
    dp.register_on_shutdown(stop_bot)

    # Запуск бота
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=start_bot,
        on_shutdown=stop_bot,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
