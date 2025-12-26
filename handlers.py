import json
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery
from telebot import types


async def start(message: Message, bot: AsyncTeleBot): 
    await bot.delete_message(message.chat.id, message.message_id)
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Стресс и мозг", callback_data="vibor_1"))
    markup.add(types.InlineKeyboardButton("Кишечник и микробиота", callback_data="vibor_2"))
    markup.add(types.InlineKeyboardButton("Биологические механизмы", callback_data="vibor_3"))
    markup.add(types.InlineKeyboardButton("Питание и стресс", callback_data="vibor_4"))
    markup.add(types.InlineKeyboardButton("Практические рекомендации", callback_data="vibor_5"))
    
    welcome_text = (
        "👋 Привет! Я бот-помощник по теме стресса и его влияния на организм.\n\n"
        "Здесь ты можешь узнать о взаимосвязи стресса, кишечника и питания, "
        "а также получить практические рекомендации.\n\n"
        "👇 Выбери одну из интересующих тебя тем ниже:"
    )
    
    await bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


async def button(message: Message, bot: AsyncTeleBot):
    await bot.delete_message(message.chat.id, message.message_id)
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Стресс и мозг", callback_data="vibor_1"))
    markup.add(types.InlineKeyboardButton("Кишечник и микробиота", callback_data="vibor_2"))
    markup.add(types.InlineKeyboardButton("Биологические механизмы", callback_data="vibor_3"))
    markup.add(types.InlineKeyboardButton("Питание и стресс", callback_data="vibor_4"))
    markup.add(types.InlineKeyboardButton("Практические рекомендации", callback_data="vibor_5"))
    
    await bot.send_message(
        message.chat.id, 
        "Выберите одну из интересующих вас тем ниже:", 
        reply_markup=markup
    )


async def show_main_menu(chat_id: int, bot: AsyncTeleBot):
    """Функция для отображения главного меню (выбора тем)"""
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Стресс и мозг", callback_data="vibor_1"))
    markup.add(types.InlineKeyboardButton("Кишечник и микробиота", callback_data="vibor_2"))
    markup.add(types.InlineKeyboardButton("Биологические механизмы", callback_data="vibor_3"))
    markup.add(types.InlineKeyboardButton("Питание и стресс", callback_data="vibor_4"))
    markup.add(types.InlineKeyboardButton("Практические рекомендации", callback_data="vibor_5"))
    
    await bot.send_message(
        chat_id, 
        "Выберите одну из интересующих вас тем ниже:", 
        reply_markup=markup
    )


async def vibor_1(call: CallbackQuery, bot: AsyncTeleBot):
    cur_vibor = call.data.split("_")[1]
    markup = types.InlineKeyboardMarkup()
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    
    if cur_vibor == "1":  # Стресс и мозг
        text = "Выберите вопрос по теме 'Стресс и мозг':"
        markup.add(types.InlineKeyboardButton("Что такое стресс и как он влияет на организм подростка?", callback_data="nevibor_1_1"))
        markup.add(types.InlineKeyboardButton("Какие признаки указывают на повышенный уровень стресса?", callback_data="nevibor_1_2"))
    
    elif cur_vibor == "2":  # Кишечник и микробиота
        text = "Выберите вопрос по теме 'Кишечник и микробиота':"
        markup.add(types.InlineKeyboardButton("Что такое микробиота кишечника и зачем она нужна?", callback_data="nevibor_2_1"))
        markup.add(types.InlineKeyboardButton("Может ли стресс начинаться в кишечнике?", callback_data="nevibor_2_2"))
    
    elif cur_vibor == "3":  # Биологические механизмы
        text = "Выберите вопрос по теме 'Биологические механизмы':"
        markup.add(types.InlineKeyboardButton("Как кишечные бактерии влияют на выработку серотонина и ГАМК?", callback_data="nevibor_3_1"))
        markup.add(types.InlineKeyboardButton("Ось «кишечник-мозг». Как блуждающий нерв передаёт сигналы?", callback_data="nevibor_3_2"))
        markup.add(types.InlineKeyboardButton("Хочу узнать больше! (статьи и исследования)", callback_data="nevibor_3_3"))
    
    elif cur_vibor == "4":  # Питание и стресс
        text = "Выберите вопрос по теме 'Питание и стресс':"
        markup.add(types.InlineKeyboardButton("Как рацион питания влияет на уровень стресса?", callback_data="nevibor_4_1"))
        markup.add(types.InlineKeyboardButton("Какие продукты могут усиливать тревожность и стресс?", callback_data="nevibor_4_2"))
    
    elif cur_vibor == "5":  # Практические рекомендации
        text = "Выберите вопрос по теме 'Практические рекомендации':"
        markup.add(types.InlineKeyboardButton("Какие группы продуктов помогут понизить уровень стресса?", callback_data="nevibor_5_1"))
        markup.add(types.InlineKeyboardButton("Что можно съесть перед экзаменом, чтобы снизить тревогу?", callback_data="nevibor_5_2"))
    
    markup.add(types.InlineKeyboardButton("Назад", callback_data="exit"))
    
    await bot.send_message(call.message.chat.id, text, reply_markup=markup)


async def exits(call: CallbackQuery, bot: AsyncTeleBot):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await show_main_menu(call.message.chat.id, bot)


async def answer_question(call: CallbackQuery, bot: AsyncTeleBot):
    with open("texts.json", "r", encoding="utf-8") as f:
        texts = json.load(f)

    with open("photos.json", "r", encoding="utf-8") as f:
        photos = json.load(f)

    await bot.delete_message(call.message.chat.id, call.message.message_id)

    parts = call.data.split("_")
    section = parts[1]
    question = parts[2]

    text = texts[section][question]

    photo_path = photos.get(section, {}).get(question)

    back_markup = types.InlineKeyboardMarkup()
    back_markup.add(types.InlineKeyboardButton("Назад", callback_data=f"vibor_{section}"))

    if photo_path:
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(
                call.message.chat.id,
                photo,
                caption=text,
                parse_mode="Markdown",
                reply_markup=back_markup
            )
    else:
        await bot.send_message(
            call.message.chat.id, 
            text,
            reply_markup=back_markup
        )


def register_all_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=["start"], pass_bot=True)
    bot.register_message_handler(button, commands=["button"], pass_bot=True)
    bot.register_callback_query_handler(vibor_1, func=lambda call: call.data.startswith("vibor_"), pass_bot=True)
    bot.register_callback_query_handler(exits, func=lambda call: call.data == "exit", pass_bot=True)
    bot.register_callback_query_handler(answer_question, func=lambda call: call.data.startswith("nevibor"), pass_bot=True)
