from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot.types import Message

from handlers import register_all_handlers

bot = AsyncTeleBot(token="7960752246:AAGbHhHQyFpHfpYJd9yFEWtBAN8BY87411Q")

async def main():
    register_all_handlers(bot)
    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())