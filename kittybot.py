import os
import requests

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler


load_dotenv()

secret_token = os.getenv('TOKEN')

updater = Updater(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'

def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat

def new_cat(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboardd=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Здравстсвуй, я КотБот! Буду рад поработать для тебя, {}.'
            ' Посмотри, кого я для тебя отыскал.').format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, get_new_image())

def main():
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    # Регистрируется обработчик MessageHandler;
    # из всех полученных сообщений он будет выбирать только текстовые сообщения
    # и передавать их в функцию new_cat()
    updater.dispatcher.add_handler(MessageHandler(Filters.text, new_cat))

    # Метод start_polling() запускает процесс polling, 
    # приложение начнёт отправлять регулярные запросы для получения обновлений.
    updater.start_polling()
    # Бот будет работать до тех пор, пока не нажмете Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
