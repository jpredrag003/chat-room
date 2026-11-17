from modules.header import print_header
from modules.user import set_user
from modules.send import send_message
from modules.list import list_users
from modules.log import _log_message

class ChatRoom:
    _instance = None

    def __new__(cls, log_file="chat_log.txt"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.current_user = None
            cls._instance.users_joined = set()
            cls._instance.user_colors = {}  # 🟢 čuvamo boju po korisniku
            cls._instance.log_file = log_file
            print_header()
        return cls._instance

        set_user(chat, users[i % len(users)])
        send_message(chat, msg)
        list_users(chat)
        _log_message(chat, "Chat ended.")



# Kreiramo chat sobu
chat = ChatRoom()

users = ["Alice", "Alisson", "Katy", "Quincy"]
i = 0

while True:
    set_user(chat, users[i % len(users)])
    i += 1

    msg = input()
    if msg.lower() == "exit":
        print("\n❌ Chat ended.")
        _log_message(chat,"Chat ended.")
        break
    elif msg.lower() == "users":
        list_users(chat)
    else:
        send_message(chat,msg)










        