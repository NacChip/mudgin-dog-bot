import telebot
import random

from telebot import types

bot = telebot.TeleBot("5435197696:AAEJeZd1GKFwr1mCbiCL7ambBjo0FVXS_ew")

@bot.message_handler(commands=['start'])
def hello(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😆 Расскажи анекдот")
    item3 = types.KeyboardButton("😜 Хочу мемасик")

    markup.add(item1, item2, item3)
    sti = open('static/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     "Здравтствуйте, {0.first_name}!\nЯ - <b>{1.first_name}</b>, ваш помощник устранения скуки.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):

    bot.send_message(message.chat.id,
                         "Нужна помощь? Давай помогу!\n /randomrange - сгенерирую для вас рандомное число\n /dialog - поговорим (бета - версия)\n /humor - анекдотик))",
                     parse_mode='html')

@bot.message_handler(commands=['randomrange'])
def randomrange_sticker(message):
    sti = open('static/coin_random.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    str=(random.randint(0, 100))
    bot.send_message(message.chat.id, str)
@bot.message_handler(commands=['meme'])
def meme(message):
    meme1 = open('static/americans_presidents.jpg', 'rb')
    meme2 = open('static/ferrari.jpg', 'rb')
    meme3 = open('static/prestuplenye_nakazanie.jpg', 'rb')
    meme4 = open('static/spor.jpg', 'rb')
    meme = random.randint(0, 3)
    if 0 == meme:
        bot.send_photo(message.chat.id, meme1)
    if 1 == meme:
        bot.send_photo(message.chat.id, meme2)
    if 2 == meme:
        bot.send_photo(message.chat.id, meme3)
    if 3 == meme:
        bot.send_photo(message.chat.id, meme4)
@bot.message_handler(commands=['dialog'])
def dialog(message):
    bot.send_message(message.chat.id, "Это экспереметальная функция пожалуйста,<i>\n 1. Пишите без ошибок\n 2. Только на русском языке\n 3. С большой буквы\n 4. Обращатся на ты</i>\nВскоре, требования мы будем уменьшать). Можете начинать!", parse_mode='html')
    dialogstart = 1
@bot.message_handler(commands=['humor'])
def humor(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Лайк 😍", callback_data='good_humor')
    item2 = types.InlineKeyboardButton("Не смешно 😒", callback_data='bad_humor')
    item3 = types.InlineKeyboardButton("Еще! 🤩", callback_data='more_humor')

    markup.add(item1, item2, item3)
    humor = random.randint(0, 5)
    if 0 == humor:
        bot.send_message(message.chat.id, 'Сын говорит отцу за ужином:\n -Папа, тебя опять в школу вызывают, я окно разбил\n -Да у вас не школа, а оранжерея какая-то.', reply_markup=markup)
    if 1 == humor:
        bot.send_message(message.chat.id, "Идут по улице дед с внуком. Видят учительницу. Дед говорит:\n -Прячься, ты же сегодня сегодня в школу не пошел.\n -Это ты прячься, я сказал, что ты умер)", reply_markup=markup)
    if 2 == humor:
        bot.send_message(message.chat.id, "Разровор сына и мамы:\n -Мама, все в школе говорят, что я врун!\n -Да ты ведь в школу не ходишь!",reply_markup=markup)
    if 3 == humor:
        bot.send_message(message.chat.id, "Встретились женщина и ребёнок:\n -А что это у вас? - <i>мальчик показывает на пальцем на живот</i>\n -Мой малыш\n -Вы его любите?\n -Очень!\n -А зачем же вы его съели?", parse_mode='html', reply_markup=markup)
    if 4 == humor:
        bot.send_message(message.chat.id, "Кролик спрашивает:\n -Винни, кто съел мед?\n -Не знаю.\n -А ещё хочешь?\n -ДА! 😝", reply_markup=markup)
    if 5 == humor:
        bot.send_message(message.chat.id, "Внук спрашивает у бабушки:\n -Бабуля, как называется эта ягода?\n -Чёрная смородина.\n -Почему же она красная?\n -Просто она ещё зеленая 😳.", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def textmassages(message):
    if message.chat.type == 'private':
        if message.text == 'Привет' or message.text == 'Привет!' or message.text == "Приветосик" or message.text == "Хай" or message.text == "Хай!" or message.text == "Хеллоу" or message.text == "Хеллоу!":
            bot.send_message(message.chat.id, "Привет!")
        elif message.text == '🎲 Рандомное число':
            sti = open('static/coin_random.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😆 Расскажи анекдот':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Лайк 😍", callback_data='good_humor')
            item2 = types.InlineKeyboardButton("Не смешно 😒", callback_data='bad_humor')
            item3 = types.InlineKeyboardButton("Еще! 🤩", callback_data='more_humor')

            markup.add(item1, item2, item3)
            humor = random.randint(0, 5)
            if 0 == humor:
                bot.send_message(message.chat.id,
                                 'Сын говорит отцу за ужином:\n -Папа, тебя опять в школу вызывают, я окно разбил\n -Да у вас не школа, а оранжерея какая-то.',
                                 reply_markup=markup)
            if 1 == humor:
                bot.send_message(message.chat.id,
                                 "Идут по улице дед с внуком. Видят учительницу. Дед говорит:\n -Прячься, ты же сегодня сегодня в школу не пошел.\n -Это ты прячься, я сказал, что ты умер)",
                                 reply_markup=markup)
            if 2 == humor:
                bot.send_message(message.chat.id,
                                 "Разровор сына и мамы:\n -Мама, все в школе говорят, что я врун!\n -Да ты ведь в школу не ходишь!",
                                 reply_markup=markup)
            if 3 == humor:
                bot.send_message(message.chat.id,
                                 "Встретились женщина и ребёнок:\n -А что это у вас? - <i>мальчик показывает на пальцем на живот</i>\n -Мой малыш\n -Вы его любите?\n -Очень!\n -А зачем же вы его съели?",
                                 parse_mode='html', reply_markup=markup)
            if 4 == humor:
                bot.send_message(message.chat.id,
                                 "Кролик спрашивает:\n -Винни, кто съел мед?\n -Не знаю.\n -А ещё хочешь?\n -ДА! 😝",
                                 reply_markup=markup)
            if 5 == humor:
                bot.send_message(message.chat.id,
                                 "Внук спрашивает у бабушки:\n -Бабуля, как называется эта ягода?\n -Чёрная смородина.\n -Почему же она красная?\n -Просто она ещё зеленая 😳.",
                                 reply_markup=markup)
        elif message.text == '😜 Хочу мемасик':
            meme1 = open('static/americans_presidents.jpg', 'rb')
            meme2 = open('static/ferrari.jpg', 'rb')
            meme3 = open('static/prestuplenye_nakazanie.jpg', 'rb')
            meme4 = open('static/spor.jpg', 'rb')
            meme = random.randint(0, 3)
            if 0 == meme:
                bot.send_photo(message.chat.id, photo=meme1, caption='Вот, что значит - долгожитель')
            if 1 == meme:
                bot.send_photo(message.chat.id, photo=meme2, caption='Расшивровка секретная)')
            if 2 == meme:
                bot.send_photo(message.chat.id, photo=meme3, caption='Лично я резал воду ножницами')
            if 3 == meme:
                bot.send_photo(message.chat.id, photo=meme4, caption='Блин..')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить но я постоянно обновляюсь')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
            if call.message:
                if call.data == 'good_humor':
                    humor_good = random.randint(0, 3)
                    if 0 == humor_good:
                        bot.send_message(call.message.chat.id, 'Учту 😊')
                    if 1 == humor_good:
                        bot.send_message(call.message.chat.id, 'Окей (☞ﾟヮﾟ)☞')
                    if 2 == humor_good:
                        bot.send_message(call.message.chat.id, 'Понятно 😼')
                    if 3 == humor_good:
                        bot.send_message(call.message.chat.id, 'РЖАКААА 😂')
                elif call.data == 'bad_humor':
                    humor_bad = random.randint(0, 2)
                    if 0 == humor_bad:
                        bot.send_message(call.message.chat.id,
                                         'К сожалению, учесть плохие предпочтения я не могу но не забывайте: \n Я постоянно обнавляюсь')
                    if 1 == humor_bad:
                        bot.send_message(call.message.chat.id, 'Жаль 😢')
                    if 2 == humor_bad:
                        bot.send_message(call.message.chat.id, 'А мне смешно 😞')
                elif call.data == 'more_humor':
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    item1 = types.InlineKeyboardButton("Лайк 😍", callback_data='good_humor')
                    item2 = types.InlineKeyboardButton("Не смешно 😒", callback_data='bad_humor')
                    item3 = types.InlineKeyboardButton("Еще! 🤩", callback_data='more_humor')

                    markup.add(item1, item2, item3)
                    humor = random.randint(0, 5)
                    if 0 == humor:
                        bot.send_message(call.message.chat.id,
                                         'Сын говорит отцу за ужином:\n -Папа, тебя опять в школу вызывают, я окно разбил\n -Да у вас не школа, а оранжерея какая-то.',
                                         reply_markup=markup)
                    if 1 == humor:
                        bot.send_message(call.message.chat.id,
                                         "Идут по улице дед с внуком. Видят учительницу. Дед говорит:\n -Прячься, ты же сегодня сегодня в школу не пошел.\n -Это ты прячься, я сказал, что ты умер)",
                                         reply_markup=markup)
                    if 2 == humor:
                        bot.send_message(call.message.chat.id,
                                         "Разровор сына и мамы:\n -Мама, все в школе говорят, что я врун!\n -Да ты ведь в школу не ходишь!",
                                         reply_markup=markup)
                    if 3 == humor:
                        bot.send_message(call.message.chat.id,
                                         "Встретились женщина и ребёнок:\n -А что это у вас? - <i>мальчик показывает на пальцем на живот</i>\n -Мой малыш\n -Вы его любите?\n -Очень!\n -А зачем же вы его съели?",
                                         parse_mode='html', reply_markup=markup)
                    if 4 == humor:
                        bot.send_message(call.message.chat.id,
                                         "Кролик спрашивает:\n -Винни, кто съел мед?\n -Не знаю.\n -А ещё хочешь?\n -ДА! 😝",
                                         reply_markup=markup)
                    if 5 == humor:
                        bot.send_message(call.message.chat.id,
                                         "Внук спрашивает у бабушки:\n -Бабуля, как называется эта ягода?\n -Чёрная смородина.\n -Почему же она красная?\n -Просто она ещё зеленая 😳.",
                                         reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<i>Анекдот был удалён</i>",
                                  reply_markup=None, parse_mode='html'),

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)