import os
import telebot
from yt_dlp import YoutubeDL
from flask import Flask
from threading import Thread

# هذا الجزء هو السر لكي لا يتوقف Render مجدداً
app = Flask('')
@app.route('/')
def home(): return "I am alive"
def run(): app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

TOKEN = "7791823297:AAGg7KMrSEhG0qks26vLcDVSED07-25oFq0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "✅ شغال 100% وبدون توقف يا محمود!")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "http" in url:
        bot.reply_to(message, "⏳ جاري تحميل الفيديو...")
        try:
            ydl_opts = {'outtmpl': 'video.mp4', 'format': 'best'}
            with YoutubeDL(ydl_opts) as ydl: ydl.download([url])
            with open('video.mp4', 'rb') as f:
                bot.send_video(message.chat.id, f, caption="تم التحميل بنجاح 🚀")
            os.remove('video.mp4')
        except: bot.reply_to(message, "❌ خطأ في الرابط أو المحتوى")

if __name__ == "__main__":
    # تشغيل السيرفر الوهمي في الخلفية
    Thread(target=run).start()
    bot.infinity_polling()
