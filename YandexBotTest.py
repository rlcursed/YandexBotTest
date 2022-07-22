import telebot;

token = '5409363954:AAEmAbnIyMm2tTxjcAfnIU4-Ys2U5xkfvrc'

bot = telebot.Telebot(token)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):

bot.infinity_poling()

