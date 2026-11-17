# modules/user.py
import random
from modules.log import _log_message

def set_user(chatroom_instance, username: str):
    """Postavlja aktivnog korisnika, dodeljuje mu boju ako je nova osoba i prikazuje poruku."""
    if username not in chatroom_instance.user_colors:
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        chatroom_instance.user_colors[username] = f"\033[38;2;{r};{g};{b}m"

    color = chatroom_instance.user_colors[username]
    reset = "\033[0m"
    chatroom_instance.current_user = f"{color}{username}{reset}"

    if username not in chatroom_instance.users_joined:
        print(f"\n👤 {chatroom_instance.current_user} joined the chat")
        print("-"*50)
        chatroom_instance.users_joined.add(username)
        _log_message(chatroom_instance, f"{username} joined the chat")  # ✅ koristi modul