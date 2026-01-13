import os
import telebot
from yt_dlp import YoutubeDL
from flask import Flask
from threading import Thread

# سيرفر وهمي لإبقاء الخدمة المجانية تعمل
app = Flask('')
@app.route('/')
def home(): return "Bot is running!"
def run(): app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

# بيانات البوت الخاصة بك
TOKEN = "7791823297:AAGg7KMrSEhG0qks26vLcDVSED07-25oFq0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "✅ البوت شغال مجاناً 100% يا محمود!")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "http" in url:
        bot.reply_to(message, "⏳ جاري التحميل...")
        try:
            ydl_opts = {'outtmpl': 'video.mp4', 'format': 'best'}
            with YoutubeDL(ydl_opts) as ydl: ydl.download([url])
            with open('video.mp4', 'rb') as f: bot.send_video(message.chat.id, f)
            os.remove('video.mp4')
        except: bot.reply_to(message, "❌ حدث خطأ في الرابط")

if __name__ == "__main__":
    Thread(target=run).start() # تشغيل السيرفر الوهمي
    bot.infinity_polling() # تشغيل البوت
