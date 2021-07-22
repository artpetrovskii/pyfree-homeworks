import telebot

token = "1804558241:AAHoNaQAA-ykuqKqQf_fSnJV1eLmoXtpczE"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, "Ба, знакомые все лица!")

bot.polling(none_stop=True)
