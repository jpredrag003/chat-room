"""Modul za prikaz zaglavlja i uvodnih poruka."""

import os


def clear_screen() -> None:
  """Čisti ekran terminala."""
  os.system("cls" if os.name == "nt" else "clear")


def show_header() -> None:
  """Prikazuje stilizovano zaglavlje chat room-a."""
  clear_screen()
  print("=" * 50)
  print("             CHAT ROOM             ")
  print("=" * 50)
  print(" Dobrodošli! Pratite uputstva za slanje i primanje poruka.\n")
