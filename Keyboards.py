from telebot import types

import Dictionary
import telebot
import Const


def main_menu():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_goods = types.KeyboardButton(Dictionary.GOODS)
    btn_feedback = types.KeyboardButton(Dictionary.FEEDBACK)
    btn_bin = types.KeyboardButton(Dictionary.BIN)
    btn_history = types.KeyboardButton(Dictionary.HISTORY)

    markup_menu.add(btn_goods)
    markup_menu.add(btn_bin, btn_history, btn_feedback)
    return markup_menu


def lang_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text="O'zbek tili", callback_data="uz"),
        types.InlineKeyboardButton(text="Русский", callback_data="ru"),
    )
    return markup


def add_subtract_inline_btn():
    markup_menu = types.InlineKeyboardMarkup(row_width=2)
    btn_plus = [
        types.InlineKeyboardButton("+", callback_data="+"),
        types.InlineKeyboardButton("-", callback_data="-"),
    ]
    markup_menu.add(btn_plus[0], btn_plus[1])
    return markup_menu


def lang(call, bot: telebot):
    chatID = call.message.chat.id
    messageID = call.message.message_id
    try:

        bot.send_message(
            chatID, text=Dictionary.SELECTED_LANG, reply_markup=main_menu()
        )
        bot.delete_message(chatID, messageID)
    except Exception as e:
        bot.send_message(chatID, e)


def price_of_bag():
    markup = types.InlineKeyboardMarkup(row_width=1)
    # todo price_btn=types.InlineKeyboardButton(text=,callback_data=) #size+name
    # todo markup.add(price_btn)
    return markup


def quantity_bags(quantity: int, bot: telebot):
    btn_quantity = types.InlineKeyboardMarkup(1)
    btn_quantity.add(
        types.InlineKeyboardButton(str(quantity) + " шт", callback_data="quantity")
    )
    bot.edit_message_text(str(quantity) + " шт")
    return btn_quantity


def goods(bot: telebot):
    # todo
    pass


def bin(bot: telebot):
    # todo
    pass


def feedback(bot: telebot):
    # todo
    pass


def history(bot: telebot):
    # todo
    pass


def back_btn():
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back = types.KeyboardButton(Dictionary.Lang().BACK)
    user_markup.add(back)
    return user_markup


def delete_btn():
    delete = types.ReplyKeyboardMarkup(row_width=1)
    delete.add(Dictionary.Lang().DELETE_BAGS)
    return delete


def home_btn(bot: telebot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    home = types.KeyboardButton(Dictionary.Lang().HOME)
    markup.add(home)
    return markup


def delete_all_orders_btn(bot: telebot):
    # todo
    pass
