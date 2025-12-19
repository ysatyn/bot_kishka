from telebot.async_telebot import AsyncTeleBot
import asyncio

bot = AsyncTeleBot("ysatyn")

async def main():
    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main)