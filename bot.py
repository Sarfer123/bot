import telebot
from telebot import types

bot = telebot.TeleBot("5270779486:AAGX9AfoYERN_Anq05XSod_D3bN14FyCQD0")

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('🎯 Тренировки')
	item2 = types.KeyboardButton('✅Консультации')
	item3 = types.KeyboardButton('🚀 Обо мне')
	
	markup.add(item1, item2, item3)

	bot.send_message(message.from_user.id, """Привет, {0.first_name}👋 
Чем я могу тебе помочь?""".format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == '🎯 Тренировки':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item4 = types.KeyboardButton("""🏅Персональная тренировка""")
			item5 = types.KeyboardButton('🖥Онлайн-ведение')
			item7 = types.KeyboardButton('🔙Назад')
			markup.add(item4, item5, item7)

			bot.send_message(message.from_user.id, '🎯 Тренировки' , reply_markup = markup)
	   
		elif message.text == '✅Консультации':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item6 = types.KeyboardButton('🏋️Программа тренировок')
			item7 = types.KeyboardButton('🔙Назад')
			markup.add(item6, item7)

			bot.send_message(message.from_user.id, '✅Консультации' , reply_markup = markup)
		
		elif message.text == '🚀 Обо мне':
			bot.send_message(message.chat.id, """Привет👋 Меня зовут Алекс.
Я выступающий спортсмен NPC в категории men's physique & classic physique.
Дипломированный специалист в области фитнеса.""")

		elif message.text == '🔙Назад':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('🎯 Тренировки')
			item2 = types.KeyboardButton('✅Консультации')
			item3 = types.KeyboardButton('🚀 Обо мне')
	
			markup.add(item1, item2, item3)

			bot.send_message(message.from_user.id, '🔙Назад' , reply_markup = markup)

		elif message.text == '🏅Персональная тренировка':
			bot.send_message(message.chat.id, """🎯 Персональная тренировка в зале - 1 час
✅Стоимость:
1 тренировка 3000₽
10 тренировок 25000₽""")

		elif message.text == '🖥Онлайн-ведение':
			bot.send_message(message.chat.id, """🎯 Онлайн ведение

✅Стоимость: 10000₽ в месяц

1. Индивидуальная программа тренировок
2. Контроль результатов и связь 24/7
3. Рекомендации по спортивным добавкам
4. Расчёт БЖУ и составление схемы питания
5. 3 личные тренировки в зале""")

		elif message.text == '🏋️Программа тренировок':
			bot.send_message(message.chat.id, """🎯 Составление программы тренировок

✅Стоимость: 10000₽

1. Составление программы тренировок
2. Проработка программы тренировок в зале""")

bot.polling(none_stop = True)
