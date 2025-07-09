
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

user_data = {}

def start(update, context):
    user_id = update.effective_user.id
    user_data[user_id] = []
    update.message.reply_text("សូមបញ្ចូលលេខមួយៗ 🧮។ បន្ទាប់ចុច /sum ដើម្បីសរុប")

def handle_number(update, context):
    user_id = update.effective_user.id
    try:
        number = float(update.message.text)
        user_data.setdefault(user_id, []).append(number)
        update.message.reply_text(f"✅ បញ្ចូលបាន៖ {number}")
    except ValueError:
        update.message.reply_text("⛔️ សូមបញ្ចូលលេខត្រឹមត្រូវ")

def sum_numbers(update, context):
    user_id = update.effective_user.id
    total = sum(user_data.get(user_id, []))
    update.message.reply_text(f"📊 ផលបូកសរុប៖ {total}")

def reset(update, context):
    user_id = update.effective_user.id
    user_data[user_id] = []
    update.message.reply_text("🔄 បានកំណត់ឡើងវិញ")

def main():
    TOKEN = '7951803629:AAE-BBVFV5pDEMoQnjiEP-LngN3UXqnO5sM
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sum", sum_numbers))
    dp.add_handler(CommandHandler("reset", reset))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_number))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
