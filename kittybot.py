from telegram.ext import CommandHandler, Updater, Filters, MessageHandler

updater = Updater(token='5862945651:AAEQmlQ1yXGW7qRwfiOxcF3bkjh-is4vawk')

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Здравстсвуй, я КотБот!')

def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Буду рад поработать для тебя.')

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle()
