import openai
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# API keys
OPENAI_API_KEY = "your_openai_api_key"
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    update.message.reply_text(response.choices[0].text.strip())

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_with_gpt))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
