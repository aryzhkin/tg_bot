import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVER = os.getenv('SERVER', 'dev')
PORT = int(os.environ.get('PORT', '8443'))
DOMAIN = os.getenv('DOMAIN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_SUPPORT_CHAT_ID = os.getenv('TELEGRAM_SUPPORT_CHAT_ID')

if DOMAIN is None and SERVER == 'production':
    raise Exception('Please, setup .env variable DOMAIN')
    
if TELEGRAM_TOKEN is None:
    raise Exception('Please, setup .env variable TELEGRAM_TOKEN')

if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip('-').isdigit():
    raise Exception('You need to specify \'TELEGRAM_SUPPORT_CHAT_ID\' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.')


TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)

WELCOME_MESSAGE='Welcome! 👋'
REPLY_TO_THIS_MESSAGE='User above dont allow forward his messages. Reply to this message.'
WRONG_REPLY='User above dont allow forward his messages. You must reply to bot reply under user forwarded message.'