from telegram.ext import Updater

from handlers import setup_dispatcher
from settings import DOMAIN, TELEGRAM_TOKEN, PORT, SERVER

# Let's set handlers
updater = Updater(TELEGRAM_TOKEN)

dp = updater.dispatcher
dp = setup_dispatcher(dp)

# Run bot
if SERVER == 'production': # webhook mode
    print("Running bot in webhook mode cause this is prod server.")
    print(f'https://{DOMAIN}:{PORT}/' + TELEGRAM_TOKEN)
    
    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        key='./private.key',
        cert='./cert.pem',
        url_path=TELEGRAM_TOKEN,
        webhook_url=f'https://{DOMAIN}:{PORT}/' + TELEGRAM_TOKEN
    )
else: # pooling mode 
    print("Running bot in pooling mode cause this is not production server (" + SERVER + ").")

    updater.start_polling()
    updater.idle()
