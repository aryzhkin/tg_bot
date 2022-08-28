# TG_BOT (by Andrey Ryzhkin)

## 📝 Table of Contents

- [About](#about)
- [How it works](#howitworks)
- [Deployment](#deployment)
- [How to start this bot](#howtostart)
- [Contacts](#contacts)

## 🧐 About <a name = "about"></a>
This is a telegram bot for teams that helps people by answering their questions: you can gather your entire team into one tg chat, where messages from people will come, and anyone in this group can answer messages.

This bot use [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (it is under [LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html))

## 🎈 How it works <a name = "howitworks"></a>
- People write their questions to the bot
- Bot forwards messages to your group
- Members answer this question by replying to the forwarded message
- The bot forward the responce back to the author

## ⛏️ How to start this bot on your server  <a name = "howtostart"></a>
1. Create your tg-bot via [BotFather](https://t.me/BotFather) & get your API token
2. Create your tg-group and add your new bot there
3. Also add [ShowJsonBot](https://t.me/ShowJsonBot) into your group to get your chat ID (you can remove this bot after that)
4. Clone this repo to your server
4. Create file '.env', copy & fiil the evnironment variables (see '.env.example')
5. Install [docker](https://docs.docker.com/engine/install/ubuntu/) (if you haven't already done so) 
6. Run
```
docker compose build .
```
7. Run
```
docker compose up -d
```
8. In case of any problems - feel free to contact me.

## ✍️ Contacts <a name = "contacts"></a>
- My name is Andrey Ryzhkin
- Telegram: [@ryzhkin](https://t.me/ryzhkin)
- E-mail: a.ryzkin@gmail.com
