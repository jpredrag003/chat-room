"""Modul za logovanje istorije razgovora i događaja."""

import datetime


def log_message(username: str, message: str, filename: str = "chat_history.log") -> None:
  """Zapisuje poruku sa vremenskim pečatom u fajl."""
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  log_entry = f"[{timestamp}] {username}: {message}\n"
  
  try:
    with open(filename, "a", encoding="utf-8") as f:
      f.write(log_entry)
  except IOError as e:
    print(f"Greška pri upisu u log fajl: {e}")
