from flask import Flask, request
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

app = Flask(__name__)

TOKEN = os.getenv('TOKEN', '7003182603:AAFNESyvjbZuAZqo6-II_NPlzmBjQCW7L_w')
WEBHOOK_URL = 'https://tel-bot-3zjj.onrender.com'

# Create an Application object with your bot's token
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Website", web_app={'url': 'mrfard.ir'})]  # استفاده از URL `ngrok`
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the website:', reply_markup=reply_markup)

# Register the /start command handler
application.add_handler(CommandHandler("start", start))

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    update = Update.de_json(data, application.bot)
    application.update_queue.put(update)
    return 'ok'

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        webhook_url=WEBHOOK_URL
    )
