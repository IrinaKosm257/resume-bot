from telegram import Update, File
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ BOTFATHER
BOT_TOKEN = '7820337107:AAEjvHtHdxJOEnzaG6z_Ez00VyNe__KS1XU'

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Здравствуйте! Прикрепите, пожалуйста, своё резюме в формате PDF/Word. 
Необходимые данные в резюме: 
- ФИО/дата рождения;
- опыт работы;
- почта/телефон;
- все остальное на Ваше усмотрение. 
Резюме будет рассмотрено в течение недели, обратную связь направим в почте."""
    )

# Обработка присланного файла
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    file_name = file.file_name
    await update.message.reply_text(f"✅ Резюме «{file_name}» получено. Спасибо!")

    # 👇 Здесь ты указываешь свой Telegram ID (куда бот будет пересылать резюме)
    YOUR_TELEGRAM_ID = 6044985341  # Замени на свой ID

    # Перешлём файл тебе
    await context.bot.send_document(chat_id=YOUR_TELEGRAM_ID, document=file.file_id, caption=f"Новое резюме: {file_name}")

# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

print("Бот запущен...")
app.run_polling()
