from aiogram.utils import executor
from create_bot import dp

"""Bot name - @ymk.fishing"""
async def on_startup(_):
    print("Онлайн")

from handlers import client

client.register_handlers_client(dp)
client.register_handlers_knots(dp)
client.register_handlers_recepy(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)