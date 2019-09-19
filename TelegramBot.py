import telebot


import Keyboards
import Const
import Dictionary

from telebot import types


quantity = 0

bot = telebot.TeleBot(Const.API_TOKEN)


@bot.message_handler(commands=["start"])
def start_menu(m):
    message = m.chat.id
    bot.send_message(
        message, Const.enter_message, reply_markup=Keyboards.lang_inline_keyboard()
    )


@bot.message_handler(commands=["help"])
def help_command(m):
    pass


@bot.message_handler(commands=["lang"])
def lang_command(m):
    bot.send_message(
        m.chat.id,
        Const.choose_language,
        reply_markup=Keyboards.lang_inline_keyboard(),
        parse_mode="HTML",
    )


@bot.callback_query_handler(func=lambda call: call.data)
def lang(call):

    Keyboards.lang(call, bot)
    bot.send_message(call.message.chat.id, Dictionary.WELCOME)


# @bot.callback_query_handler(func=lambda call:call.data==todo)
# def the_bag_buy(m):
#     message=m.chat.id
#     bot.send_message(message,reply_markup=)
#     bot.send_photo(reply_markup=Keyboards.add_subtract_inline_btn())
#     bot.send_message()


@bot.message_handler(content_types=['text'], func=lambda text: text.text == Dictionary.GOODS)
def goods(message):
    m = message.chat.id

    bot.send_message(m, Dictionary.SELECT_BAG, reply_markup=Keyboards.back_btn())
    # for i in Goods.select():
    #     bot.send_photo(m,i.bag_name, reply_markup=Keyboards.back_btn())
    #     bot.send_message(m,reply_markup=Keyboards.price_of_bag())

    pass


@bot.message_handler(content_types=['text'], func=lambda text: text.text == Dictionary.HISTORY)
def history(message):
    m = message.chat.id

    bot.send_message(m, Dictionary.HISTORY_BTN_PRESSED)

    pass


@bot.message_handler(content_types=['text'], func=lambda text: text.text == Dictionary.BIN)
def bin(message):
    m = message.chat.id

    bot.send_message(m, Dictionary.BIN_BTN_PRESSED)

    pass


@bot.message_handler(content_types=['text'], func=lambda text: text.text == Dictionary.FEEDBACK)
def feedback(message):
    m = message.chat.id

    bot.send_message(m, Dictionary.FEEDBACK_BTN_PRESSED)


@bot.message_handler(content_types=['text'], func=lambda message: message.text == Dictionary.BACK)
def back_btn(m):
    bot.send_message(m.chat.id, text=Dictionary.BACK, reply_markup=Keyboards.main_menu())


@bot.message_handler(content_types=['text'], func=lambda message: message.text == Dictionary.BACK)
def home_btn(m):
    bot.send_message(m.chat.id, text=Dictionary.HOME, reply_markup=Keyboards.main_menu())


bot.polling()
