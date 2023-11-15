import telebot
from telebot import types
from knowledge_base import decision_tree

usersToCurrentQuestions = {}

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    current_question = decision_tree['starting_point']
    usersToCurrentQuestions[user_id] = current_question
    msg = 'Welcome to the ' + decision_tree['choice'] + " Bot! Let's find the best " + decision_tree['choice'] + ' for you.'
    bot.send_message(user_id, msg)

    options = decision_tree[current_question]['answers']
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(*options)
    bot.send_message(user_id, decision_tree[current_question]['question'], reply_markup=keyboard)

    bot.register_next_step_handler(message, answer_question)


def answer_question(message):
    user_id = message.from_user.id

    prev_question = usersToCurrentQuestions[user_id]
    answer = message.text
    if answer not in decision_tree[prev_question]['answers']:
        bot.send_message(user_id, "Please use the provided buttons to answer")
        options = decision_tree[prev_question]['answers']
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.add(*options)
        bot.send_message(user_id, decision_tree[prev_question]['question'], reply_markup=keyboard)
        bot.register_next_step_handler(message, answer_question)
        return

    current_question = decision_tree[prev_question]['next_question'][answer]
    usersToCurrentQuestions[user_id] = current_question

    if current_question.startswith('ANSWER'):
        msg = "The best " + decision_tree['choice'] + " for you is " + current_question.replace('ANSWER ', "")
        bot.send_message(user_id, msg, reply_markup=types.ReplyKeyboardRemove())
        del usersToCurrentQuestions[user_id]
    else:
        next_question = decision_tree[current_question]['question']
        options = decision_tree[current_question]['answers']
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.add(*options)
        bot.send_message(user_id, next_question, reply_markup=keyboard)
        bot.register_next_step_handler(message, answer_question)

bot.polling()



# current_question = 'blockchain_type'
# while True:
#     answer = input(decision_tree[current_question]['question'])
#     current_question = decision_tree[current_question]['next_question'][answer]
#     if current_question.startswith('ANSWER'):
#             print('The best blockchain for you is', current_question.replace('ANSWER ', ""))
#             break
