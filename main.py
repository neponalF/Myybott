import logging
from telegram import *
from telegram.ext import *
import response
API_TOKEN = '6599168926:AAHzOSO8Pv74KTSa7m8dWbZ_R5XAyIGlfUc'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# __


async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт, користувач")


async def info(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Цей бот створений для курсу Python")


async def errors(update, context):
    logging.error(f"Update {update} caused error {context.error}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{context.error}")

# Огляд, що написав користувач


async def handle_message(update, context):
    logging.info(f"Update {update.message.chat.id} says: {update.message}")
    text = str(update.message.text).lower()
    responses = response.get_response(text)

    # Відповідь бота
    await update.message.reply_text(responses)

if __name__ == "__main__":

    app = ApplicationBuilder().token(
        API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('info', info))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(errors)

    app.run_polling()
