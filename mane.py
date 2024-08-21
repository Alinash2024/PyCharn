import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # replace with your bot token

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Добро пожаловать в нашу гостиницу! Как я могу вам помочь?')

def book_room(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Чтобы забронировать номер, пожалуйста, отправьте мне следующие данные:\n\nДата заезда\nДата выезда\nКоличество гостей\nТип номера (одиночный, двойной, люкс)')

def room_info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Номера в нашей гостинице:\n\n* Одиночный: 5000₽ в сутки\n* Двойной: 8000₽ в сутки\n* Люкс: 12000₽ в сутки')

def services(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Наши услуги:\n\n* Wi-Fi\n* Завтрак\n* Уборка номера\n* Трансфер из аэропорта')

def contact(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Контакты:\n\nТелефон: +7 123 456 78 90\nEmail: [info@hotel.ru](mailto:info@hotel.ru)\nАдрес: Москва, ул. Ленина, 123')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('book_room', book_room))
    dp.add_handler(CommandHandler('room_info', room_info))
    dp.add_handler(CommandHandler('services', services))
    dp.add_handler(CommandHandler('contact', contact))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()