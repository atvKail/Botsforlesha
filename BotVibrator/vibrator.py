import telebot
import random
import config

bot = telebot.TeleBot("5028812401:AAEEgqcQBFW8TScSIjotj__lVb9ygShHLvk")


@bot.message_handler(commands="help")
def helpins(msg):
    bot.send_message(msg.from_user.id, "По вопросам получения кода доступа, "
                                       "обращайтесь к аминистратору(https://t.me/Alexeyalexvl)")


@bot.message_handler(commands="getnewkeys")
def geting(msg):
    bot.send_message(msg.from_user.id, "Введите код доступа администратора!!!")
    bot.register_next_step_handler(msg, password_admin)


def password_admin(msg):
    file = config.compare_pass()
    if msg.text == file:
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        password = "".join(random.sample(abc, 10))
        bot.send_message(msg.from_usr.id, password)
        config.write_newgenpass(password)


@bot.message_handler(commands="input")
def welcome(msg):
    bot.send_message(msg.from_user.id, "Введите код доступа!!!")
    bot.register_next_step_handler(msg, writepass)


def writepass(msg):
    if msg.text == config.look_input():
        keyboard = telebot.types.InlineKeyboardMarkup().add(
            telebot.types.InlineKeyboardButton("WELCOME", url="https://t.me/stavkiben"))
        bot.send_message(msg.from_user.id, "Добро пожаловать, в наш коллектив", reply_markup=keyboard)


@bot.message_handler(commands="inf")
def get_inf(msg):
    bot.send_message(msg.from_user.id, "Бот сделан для входа в закрытый канал.")


@bot.message_handler(commands="upadmin")
def pasudateadmin(msg):
    bot.send_message(msg.from_user.id, "Введите код доступа администратора!!!")
    bot.register_next_step_handler(msg, update)


def update(msg):
    if msg.text == config.compare_pass():
        bot.register_next_step_handler(msg, up)


def up(msg):
    config.updateadmin(msg.text)
    bot.send_message(msg.from_user.id, "Done")


bot.polling(non_stop=True)
