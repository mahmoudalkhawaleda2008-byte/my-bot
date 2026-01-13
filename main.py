import os
import telebot
from yt_dlp import YoutubeDL

# التوكن الخاص بك
TOKEN = "7791823297:AAGg7KMrSEhG0qks26vLcDVSED07-25oFq0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "✅ أهلاً محمود! البوت يعمل الآن بنجاح على سيرفر Render.")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "http" in url:
        sent_msg = bot.reply_to(message, "⏳ جاري المعالجة والتحميل...")
        try:
            ydl_opts = {
                'outtmpl': 'video.mp4',
                'format': 'best',
                'quiet': True
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            with open('video.mp4', 'rb') as f:
                bot.send_video(message.chat.id, f, caption="تم التحميل بواسطة بوت محمود 🚀")
            
            os.remove('video.mp4')
        except Exception as e:
            bot.reply_to(message, "❌ حدث خطأ، تأكد من صحة الرابط.")

bot.infinity_polling()
