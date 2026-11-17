import telebot
import requests

TOKEN = "9071470594:AAFRoLM7b5cP1G7f14nQnglUwfGjzlJwBEw"
API_URL = "https://my-perfect-like-api-production.up.railway.app"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 Bot ON hai! UID bhejo: /like 123456789")

@bot.message_handler(commands=['like'])
def like(m):
    try:
        uid = m.text.split()[1]
        bot.reply_to(m, "⏳ Like bhej raha hun...")
        r = requests.get(f"{API_URL}/like?uid={uid}&server_name=PK", timeout=30)
        bot.reply_to(m, f"✅ Done! {r.text[:1000]}")
    except:
        bot.reply_to(m, "Aise likho: /like 123456789")

bot.polling()
