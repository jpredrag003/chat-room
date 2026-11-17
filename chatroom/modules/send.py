"""Modul zadužen za slanje poruka."""

import socket


def send_message(sock: socket.socket, message: str, encoding: str = "utf-8") -> bool:
  """Šalje formatiranu poruku preko socket veze."""
  try:
    if not message.strip():
      return False
    sock.sendall(message.encode(encoding))
    return True
  except socket.error as e:
    print(f"Greška pri slanju poruke: {e}")
    return False
