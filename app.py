import telebot
from dotenv import load_dotenv
import os
load_dotenv()
# laod the token from .env file
def main():
    token = os.getenv('API_KEY')

    bot = telebot.TeleBot(token=token, parse_mode=None)

    # this bot will send message to a specific user with id = user_id
    # and send message everyday at 6:30 AM
    user_id = os.getenv('USER_ID')
    # this is the message that will be sent
    def send_message(user_id, message):
        bot.send_message(user_id, message)


if __name__ == '__main__':
    main()