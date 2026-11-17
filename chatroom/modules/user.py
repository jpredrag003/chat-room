"""Modul za upravljanje korisnicima i autentifikacijom."""


def get_username() -> str:
  """Traži od korisnika da unese validno korisničko ime."""
  while True:
    username = input("Unesite vaše korisničko ime: ").strip()
    if username:
      if len(username) <= 20:
        return username
      print("Greška: Korisničko ime može imati najviše 20 karaktera.")
    else:
      print("Greška: Korisničko ime ne može biti prazno.")
