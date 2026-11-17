"""Glavna ulazna tačka za Chatroom aplikaciju."""

import sys
import os

# Dodavanje putanje radi lakšeg importovanja modula ukoliko se pokreće direktno
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.header import show_header
from modules.user import get_username
from modules.list import display_user_list
from modules.log import log_message
from modules.send import send_message


def main() -> None:
  """Glavna petlja aplikacije."""
  show_header()
  username = get_username()
  print(f"\nUspešno ste prijavljeni kao: **{username}**\n")

  # Primer osnovne demonstracije modula
  sample_users = ["Admin", "Nikola", "Ana"]
  display_user_list(sample_users)

  print("Unesite poruku za slanje (ili 'exit' za izlaz):")
  while True:
    try:
      msg = input(f"{username} > ")
      if msg.lower() == "exit":
        print("Izlaz iz aplikacije. Doviđenja!")
        break
      
      log_message(username, msg)
      print(Sačuvano u log i poslato.)
    except KeyboardInterrupt:
      print("\nPrekinuto od strane korisnika.")
      break


if __name__ == "__main__":
  main()








        
