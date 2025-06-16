from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os

# Читаем токен и chat_id из переменных окружения
TOKEN = os.getenv('TOKEN')
CHANNEL_CHAT_ID = int(os.getenv('CHANNEL_CHAT_ID'))

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Привет! Отправь своё анонимное поздравление — я передам его в общий канал. Все поздравления полностью анонимны!"
    )

# Обрабатываем все текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    message_to_channel = f"🎊 Новое анонимное поздравление:\n\n{user_message}"
    await context.bot.send_message(chat_id=CHANNEL_CHAT_ID, text=message_to_channel)
    await update.message.reply_text("✅ Твоё поздравление успешно отправлено!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
