from telebot import TeleBot

bot = TeleBot("1844003407:AAFMTNPOy4d5eHAdHRUxzg8xwi90vd1oXu4")
admin = "1668143308"

@bot.message_handler(commands=['start'])
def send_hello(message):
  chat_id = message.from_user.id
  text = f"Assalomu alaykum @{message.from_user.first_name}!\nSiz yuborgan barcha fikr va mulohazalar @muzrob_uz adminigiga yetkaziladi. Marhamat, xabaringizni yuboring."
  
  if str(chat_id) == admin:
    bot.send_message(admin, "Assalomu alaykum admin, xush kelibsiz...")
  else:
    bot.send_message(chat_id, text)
    
    
@bot.message_handler(func=lambda message:True)
def chat(message):
  text = message.text
  chatId = message.chat.id
  reply = message.reply_to_message

  if reply:
    bot.send_message(message.reply_to_message.forward_from.id, text)
  else:
    bot.forward_message(admin, message.from_user.id, message.message_id)
    bot.send_message(message.chat.id, "Xabaringiz jo'natildi...")

bot.polling()