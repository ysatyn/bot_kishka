from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery
from telebot import types


async def start(message: Message, bot: AsyncTeleBot): 
    await bot.send_message(message.chat.id, "Привет")


async def button(message: Message, bot: AsyncTeleBot):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Стресс и мозг", callback_data="vibor_1"))
    markup.add(types.InlineKeyboardButton("Кишечник и микробиота", callback_data="vibor_2"))
    markup.add(types.InlineKeyboardButton("Биологические механизмы", callback_data="vibor_3"))
    markup.add(types.InlineKeyboardButton("Питание и стресс", callback_data="vibor_4"))
    markup.add(types.InlineKeyboardButton("Практические рекомендации", callback_data="vibor_5"))
    await bot.send_message(message.chat.id, "Выберите одну из интерисующих вас тем ниже", reply_markup=markup)


async def vibor_1(call: CallbackQuery, bot: AsyncTeleBot):
    cur_vibor = call.data.split("_")[1]
    markup = types.InlineKeyboardMarkup()
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    
    if cur_vibor == "1":  # Стресс и мозг
        text = "Скип"
        markup.add(types.InlineKeyboardButton("Что такое стресс и как он влияет на организм подростка?", callback_data="nevibor_1_1"))
        markup.add(types.InlineKeyboardButton("Какие признаки указывают на повышенный уровень стресса?", callback_data="nevibor_1_2"))
    
    elif cur_vibor == "2":  # Кишечник и микробиота
        text = "Скип"
        markup.add(types.InlineKeyboardButton("Что такое микробиота кишечника и зачем она нужна?", callback_data="nevibor_2_1"))
        markup.add(types.InlineKeyboardButton("Может ли стресс начинаться в кишечнике?", callback_data="nevibor_2_2"))
    
    elif cur_vibor == "3":  # Биологические механизмы
        text = "Скип"
        markup.add(types.InlineKeyboardButton("Как кишечные бактерии влияют на выработку серотонина и ГАМК?", callback_data="nevibor_3_1"))
        markup.add(types.InlineKeyboardButton("Ось «кишечник-мозг». Как блуждающий нерв передаёт сигналы?", callback_data="nevibor_3_2"))
        markup.add(types.InlineKeyboardButton("Хочу узнать больше! (статьи и исследования)", callback_data="nevibor_3_3"))
    
    elif cur_vibor == "4":  # Питание и стресс
        text = "Скип"
        markup.add(types.InlineKeyboardButton("Как рацион питания влияет на уровень стресса?", callback_data="nevibor_4_1"))
        markup.add(types.InlineKeyboardButton("Какие продукты могут усиливать тревожность и стресс?", callback_data="nevibor_4_2"))
    
    elif cur_vibor == "5":  # Практические рекомендации
        text = "Скип"
        markup.add(types.InlineKeyboardButton("Какие группы продуктов помогут понизить уровень стресса?", callback_data="nevibor_5_1"))
        markup.add(types.InlineKeyboardButton("Что можно съесть перед экзаменом, чтобы снизить тревогу?", callback_data="nevibor_5_2"))
    
    markup.add(types.InlineKeyboardButton("Назад", callback_data="exit"),)
    
    await bot.send_message(call.message.chat.id, text, reply_markup=markup)


async def exits(call: CallbackQuery, bot: AsyncTeleBot):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await button(call.message, bot)


def register_all_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=["start"], pass_bot=True)
    bot.register_message_handler(button, commands=["button"], pass_bot=True)
    bot.register_callback_query_handler(vibor_1, func= lambda call: call.data.startswith("vibor_"), pass_bot=True)
    bot.register_callback_query_handler(exits, func= lambda call: call.data.startswith("exit"), pass_bot=True)