from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

# Ваш токен Telegram бота
TOKEN = '7513695715:AAGeGvvtQyTsa4yEHoQRRRPeVq7LDNc_FjE'

# Flask приложение
app = Flask(__name__)

# Настройка бота
bot = Bot(token=TOKEN)

# Настройка диспетчера
dispatcher = Dispatcher(bot, None, use_context=True)

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Нажми на ссылку, чтобы сыграть в игру: https://hhh12s.github.io/internetsafetygame.com/")

# Регистрация обработчиков
dispatcher.add_handler(CommandHandler("start", start))

# Webhook обработчик
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# Основной маршрут для проверки
@app.route("/", methods=["GET"])
def index():
    return "Бот работает!", 200

# Запуск приложения
if __name__ == "__main__":
    # Укажите ваш публичный URL
    PUBLIC_URL = "https://hhh12s.github.io/internetsafetygame.com/"
    
    # Устанавливаем Webhook
    bot.set_webhook(f"{PUBLIC_URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=8443)
