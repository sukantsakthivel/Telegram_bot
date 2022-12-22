
import telegram.ext

Token = "5932219013:AAGkThVJh-7Atqq1HLoQ6TfMP_PgkxrWTcw"
updater = telegram.ext.updater("5932219013:AAGkThVJh-7Atqq1HLoQ6TfMP_PgkxrWTcw", use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("Hello! Welcome to S4")
def end(update, context):
    update.message.reply_text("Arigato(Thank you)")
dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('end',end))
updater.start_polling(0)
updater.idle()