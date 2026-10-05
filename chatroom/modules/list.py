# modules/list.py
def list_users(self):
    """Prikazuje sve korisnike i njihove boje."""
    print("\n📋 Users in chat:")
    for user in self.users_joined:
        color = self.user_colors[user]
        reset = "\033[0m"
        print(f"- {color}{user}{reset}")
    print("-"*50)