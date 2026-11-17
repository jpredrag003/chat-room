"""Unit testovi za Chatroom komponente."""

import unittest
from chatroom.modules.user import get_username
from chatroom.modules.log import log_message
import os


class TestChatroomModules(unittest.TestCase):

  def test_log_message(self):
    test_file = "test_chat.log"
    log_message("TestUser", "Zdravo svete!", test_file)
    self.assertTrue(os.path.exists(test_file))
    
    with open(test_file, "r", encoding="utf-8") as f:
      content = f.read()
      self.assertIn("TestUser: Zdravo svete!", content)
      
    # Cleanup
    if os.path.exists(test_file):
      os.remove(test_file)


if __name__ == "__main__":
    unittest.main()