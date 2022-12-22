
import telegram.ext

Token = "Your_Telegram_Bot_API_Token"
updater = telegram.ext.updater("Your_Telegram_Bot_API_Token", use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("Hello! Welcome to S4")
def end(update, context):
    update.message.reply_text("Arigato(Thank you)")
dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('end',end))
updater.start_polling(0)
updater.idle()
