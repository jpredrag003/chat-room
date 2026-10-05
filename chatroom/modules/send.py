# modules/send.py
from modules.log import _log_message
import emoji
from datetime import datetime

def send_message(chatroom_instance, message: str):
    """Šalje poruku sa timestampom i podrškom za emoji, i čuva je u fajl."""
    if not chatroom_instance.current_user:
        print("⚠️ No active user. Set a user first.")
        return

    if len(message) > 5000:
        print("⚠️ Poruka je predugačka, maksimalno 5000 karaktera.")
        return

    timestamp = datetime.now().strftime("%H:%M:%S")
    safe_message = emoji.emojize(message, language='alias')
    print(f"[{timestamp}] {chatroom_instance.current_user}: {safe_message}")
    print("-"*50)

    # Ukloni ANSI kod da logujemo samo username
    username_plain = chatroom_instance.current_user.replace("\033[0m", "").split("m")[-1]
    _log_message(chatroom_instance, f"[{timestamp}] {username_plain}: {safe_message}")  # ✅ koristi modul