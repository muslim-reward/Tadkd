from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# قراءة التوكن من متغير البيئة
TOKEN = os.getenv("BOT_TOKEN")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚧 السيرفر تحت التطوير! الرجاء المحاولة لاحقاً.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("🔹 البوت جاهز للرد التلقائي...")
app.run_polling()
