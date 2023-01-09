from telegram import Bot

bot = Bot(token='5862945651:AAGOB6kEbeXLHGV5OYVPwpRJJZ1yvMMrLEQ')
chat_id = 395058176
text = 'Здравствуй!'
bot.send_message(chat_id, text)