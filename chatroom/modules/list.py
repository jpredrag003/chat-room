"""Modul za upravljanje i prikaz liste aktivnih korisnika."""


def display_user_list(users: list) -> None:
  """Prikazuje list trenutno povezanih korisnika."""
  print("\n--- Aktivni korisnici ---")
  if not users:
    print("Nema drugih korisnika na mreži.")
  else:
    for idx, user in enumerate(users, 1):
      print(f"{idx}. {user}")
  print("-" * 25)
