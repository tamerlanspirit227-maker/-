import telebot

TOKEN = "8279354209:AAGfqXYjzlqKSQErxxpUdOB_HiRouQCTl-Y"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Это твой бот,скоро он будет уметь много всякого.")


@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text.lower()
    if "привет" in text:
        bot.send_message(message.chat.id, "Привет! Как твои дела?")
    elif "как дела" in text:
        bot.send_message(message.chat.id, "Отлично! А у тебя?")
    elif "/cat" in text:
        bot.send_photo(message.chat.id, photo= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgVfHORQFLyUf_rNove-xUmxIskDeMJ63REz_YIMQ6S0vCyQdkBvJos4igKspvCgpqnpy8h0xM--1uckzZIxDgyoHy37-MowkF-YzvVx8")
    elif "/gif" in text:
        bot.send_animation(message.chat.id, animation="https://www.ixbt.com/img/x780/n1/news/2020/5/1/tenor-google.gif")
    elif "/sticker" in text:
        bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEPe0Jo3R4MwWasOVgDnEF4Ko4FzXVFEAACfDEAAvrjwEkOkbWwvM-KQjYE")
    else:
        bot.send_message(message.chat.id, "Извини, я не понимаю. Попробуй написать что-то другое.")
#Точка входа
if __name__ == "__main__":
    bot.polling(none_stop=True) # Запуск бота