from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

predictions = [
    "🏏 MI will win",
    "🦁 CSK will win",
    "🔵 RCB will win",
    "⚠️ Very risky match",
    "💀 Avoid betting today"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏏 IPL Prediction Bot\n\nUse /predict"
    )

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🔮 Prediction: {random.choice(predictions)}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predict", predict))

app.run_polling()
