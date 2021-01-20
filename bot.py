import telebot

bot = telebot.TeleBot('ban')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
         bot.reply_to(message, f"Я бот. Приятно познакомиться", {message.from_user.first_name})
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()
