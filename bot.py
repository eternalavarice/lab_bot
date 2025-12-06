import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

BOT_TOKEN = ""

CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

# Список фактов про котов
CAT_FACTS = [
    "Кошки спят около 70% своей жизни.",
    "Кошки могут издавать более 100 разных звуков.",
    "Кошки чистятся, вылизывая шерсть до 50% своего времени.",
    "Кошки видят лучше в темноте, чем люди.",
    "Кошки мурлыкают не только когда счастливы, но и когда больны или тревожны."
]

# Команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет! Я котобот 😺\n\n"
        "Вот что я умею:\n"
        "/random - случайная картинка котика\n"
        "/fact - случайный факт про котов\n"
        "/meow - мяу-мяу\n"
        "/help - помощь по командам"
    )
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "/random - картинка котика\n"
        "/fact - факт про котов\n"
        "/meow - мяу-мяу\n"
        "/help - список команд"
    )
    await update.message.reply_text(text)

async def random_cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(CAT_API_URL)
        data = response.json()
        image_url = data[0]['url']
        await update.message.reply_photo(photo=image_url)
    except Exception as e:
        await update.message.reply_text("Упс, не удалось получить котика 😿")

async def cat_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = random.choice(CAT_FACTS)
    await update.message.reply_text(f"🐱 {fact}")

async def meow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    meows = ["Мяу 🐾", "Мяууу 😸", "МЯУ! 😹", "мяу-мяу 😽"]
    await update.message.reply_text(random.choice(meows))

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("random", random_cat))
    app.add_handler(CommandHandler("fact", cat_fact))
    app.add_handler(CommandHandler("meow", meow))

    print("Котобот запущен 🐾")
    app.run_polling()

if __name__ == "__main__":
    main()
