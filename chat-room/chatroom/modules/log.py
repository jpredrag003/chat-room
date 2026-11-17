# modules/log.py
def _log_message(chatroom_instance, text: str):
    """Upisuje poruku u log fajl."""
    with open(chatroom_instance.log_file, "a", encoding="utf-8") as f:
        f.write(text + "\n")