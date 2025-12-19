from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message


async def start(message: Message, bot: AsyncTeleBot): 
    await bot.send_message(message.chat.id, "Привет")

def register_all_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=["start"], pass_bot=True)