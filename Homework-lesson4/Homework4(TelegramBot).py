"""
Task 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
які містять дві голосні літери підряд.
Тут створенно телеграм бота, щоб з ним взаємодіяти необіхдно знайти його
1) Name = MyHomework4
2) Username = @MyHomework4Bot
3) link = https://t.me/MyHomework4Bot
"""
import telebot

my_bot = telebot.TeleBot("5578609427:AAGxMpuHGorijL-2vNMSwZt7eU2FN57fQIo")

@my_bot.message_handler(commands=['start'])
def start(message):
    user_name = f"{message.from_user.first_name}"
    mess = f"Вітаю {user_name}! \nВведіть речення, щоб визначати кількість слів, які містять дві голосні літери підряд"
    my_bot.send_message(message.chat.id, mess)


@my_bot.message_handler()
def message_from_user(message):
    vowels_tuple = ("a", "e", "i", "o", "u", "y", "а", "е", "є", "и", "і", "ї", "о", "у", "ю", "я")
    vowels_pair_list = []
    for letter1 in vowels_tuple:
        for letter2 in vowels_tuple:
            vowels_pair_list.append(letter1 + letter2)
    every_word_number = 0
    my_string = message.text.lower()
    for every_word in my_string.split():
        for every_pair in vowels_pair_list:
            if every_word.count(every_pair):
                every_word_number += 1
                break  # Тут break для того щоб рахувало слова як "aakii" як 1
    result_text = f"Кількість слів у \"{my_string}\" які містять дві голосні літери підряд = {every_word_number}"
    my_bot.send_message(message.chat.id, result_text)


my_bot.polling(none_stop=True)
