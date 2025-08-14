from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# قراءة التوكن من ملف .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# رسالة تلقائية لأي رسالة واردة
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚧 السيرفر تحت التطوير! الرجاء المحاولة لاحقاً.")

# بناء التطبيق
app = ApplicationBuilder().token(TOKEN).build()

# اعتراض أي رسالة نصية
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("🔹 البوت جاهز للرد التلقائي...")
app.run_polling()
