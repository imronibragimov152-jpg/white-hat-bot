import requests
import random
import time
import os
import threading
from datetime import datetime
from flask import Flask

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID", "@imron_white")

POSTS = [
    "🔐 White Hat nima?\n\nWhite Hat - bu qonuniy xaker. Tizimni buzish uchun emas, himoya qilish uchun ishlaydi.",
    "🛡️ Phishingdan saqlaning!\n\nTelegramda 'Sizga pul tushdi' degan linkka kirmang.",
    "💻 Bugungi maslahat: Parollaringizni 1Password da saqlang va 2FA ni yoqing!",
    "🚨 Kiberxavfsizlik: SQL injection hali ham eng katta xavf. Har doim prepared statements ishlating!",
    "🎯 White Hat bo'lish uchun:\n1. Linux o'rganing\n2. Networking - TCP/IP\n3. TryHackMe.com da mashq qiling!",
    "🔍 Bugungi tool: Nmap\n\nnmap -sV 192.168.1.1 - portlarni tekshirish uchun eng kuchli vosita.",
    "🧠 Social Engineering dan saqlaning! Hech kim sizdan parol so'ramasligi kerak.",
]

IMAGES = [
    "https://i.imgur.com/8Km9tLL.png",
    "https://i.imgur.com/XsV6J2p.jpeg",
    "https://i.imgur.com/Jvh1OQm.jpeg",
    "https://i.imgur.com/7p6Yb0F.png"
]

def send_post():
    if not BOT_TOKEN:
        print("BOT_TOKEN yoq!")
        return
    post = random.choice(POSTS)
    image_url = random.choice(IMAGES)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    data = {"chat_id": CHANNEL_ID, "photo": image_url, "caption": post}
    try:
        r = requests.post(url, data=data, timeout=30)
        now = datetime.now().strftime("%H:%M:%S")
        if r.status_code == 200:
            print(f"[{now}] ✅ Post yuborildi!")
        else:
            print(f"[{now}] ❌ Xato: {r.text[:200]}")
    except Exception as e:
        print(f"Xatolik: {e}")

def bot_loop():
    print("🤖 Bot loop boshlandi! Har 2 soatda post yuboradi")
    time.sleep(10)
    send_post()
    while True:
        print("Keyingi post 2 soatdan keyin...")
        time.sleep(7200)
        send_post()

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 White Hat Bot 24/7 ishlayapti! ✅"

if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
