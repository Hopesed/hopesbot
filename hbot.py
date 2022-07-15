import telebot
from telebot import types

junr = 0
url = '[Кликни](https://animego.org/anime?sort=r.rating&direction=desc)'

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reting = types.KeyboardButton('Аниме по рейтингу')
    janr = types.KeyboardButton('Аниме по жанру')

    markup.add(reting, janr)
    bot.send_message(message.chat.id,f'Хая {message.from_user.first_name}, я помогу тебе найти годное аниме', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Аниме по рейтингу"):
        bot.send_message(message.chat.id, text="сам смотри")
        bot.send_message(message.chat.id, url, parse_mode='MarkdownV2')
    elif (message.text == "Аниме по жанру"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        bezumiya = types.KeyboardButton('Безумия')
        boy = types.KeyboardButton('Боевые искусства')
        vampire = types.KeyboardButton('Вампиры')
        war = types.KeyboardButton('Военное')
        garem = types.KeyboardButton('Гарем')
        demon = types.KeyboardButton('Демоны')
        detektiv = types.KeyboardButton('Детектив')
        kids = types.KeyboardButton('Детское')
        drama = types.KeyboardButton('Драма')
        game = types.KeyboardButton('Игры')
        history = types.KeyboardButton('История')
        fun = types.KeyboardButton('Комеди')
        space = types.KeyboardButton('Космос')
        magic = types.KeyboardButton('Магия')
        car = types.KeyboardButton('Машины')
        music = types.KeyboardButton('Музыка')
        parodiya = types.KeyboardButton('Пародия')
        povsednevka = types.KeyboardButton('Повседневность')
        police = types.KeyboardButton('Полиция')
        adventure = types.KeyboardButton('Приключения')
        psix = types.KeyboardButton('Психологическое')
        romantik = types.KeyboardButton('Романтика')
        samurai = types.KeyboardButton('Самураи')
        sverxestestvenoe = types.KeyboardButton('Сверхъестевственное')
        sedze = types.KeyboardButton('Сёдзе')
        sedzea = types.KeyboardButton('Сёдзе Ай')
        senen = types.KeyboardButton('Сёнэн')
        senena = types.KeyboardButton('Сёнэн-Ай')
        sport = types.KeyboardButton('Спорт')
        supersila = types.KeyboardButton('Суперсила')
        senan = types.KeyboardButton('Сэйнэн')
        triller = types.KeyboardButton('Триллер')
        horror = types.KeyboardButton('Хоррор')
        fantastic = types.KeyboardButton('Фантастика')
        fantesi = types.KeyboardButton('Фэнтези')
        school = types.KeyboardButton('Школа')
        ekshen = types.KeyboardButton('Экшен')
        etti = types.KeyboardButton('Этти')

        markup.add(bezumiya, boy, vampire, war, garem, demon, detektiv, kids, drama, game, history, fun, space, magic, car, music, parodiya, povsednevka, police, adventure, psix, romantik, samurai, sverxestestvenoe, sedze, sedzea, senen, senena, sport, supersila, senan, triller, horror, fantastic, fantesi, school, ekshen, etti, back)
        bot.send_message(message.chat.id, 'Выбери жанр', reply_markup=markup)

    elif (message.text == 'Назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        reting = types.KeyboardButton('Аниме по рейтингу')
        janr = types.KeyboardButton('Аниме по жанру')

        markup.add(reting, janr)
        bot.send_message(message.chat.id, f'Домой {message.from_user.first_name}, Домоооой',reply_markup=markup)




    elif (message.text == 'Безумия') or (message.text == 'Вампиры'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            da = types.KeyboardButton("Да")
            net = types.KeyboardButton("Нет")
            back = types.KeyboardButton("Назад")
            markup.add(da, net, back)
            bot.send_message(message.chat.id, text="Хочешь еще один выбрать?", reply_markup=markup)
            if message.text == "Да":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                boy = types.KeyboardButton('Боевые искусства')
                vampire = types.KeyboardButton('Вампиры')

                markup.add(boy, vampire)
                bot.send_message(message.chat.id, 'Выбери жанр', reply_markup=markup)
            elif message.text == 'Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                reting = types.KeyboardButton('Аниме по рейтингу')
                janr = types.KeyboardButton('Аниме по жанру')

                markup.add(reting, janr)
                bot.send_message(message.chat.id, f'Домой {message.from_user.first_name}, Домоооой',reply_markup=markup)


    else:
        bot.send_message(message.chat.id, text="кнопки жми олух")


bot.polling(none_stop=True)


bot.polling(none_stop=True)
