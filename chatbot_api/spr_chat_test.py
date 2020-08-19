import unittest
from server import ChatServer


class MyTestCase(unittest.TestCase):
    def test_gen_messages(self):
        messages = [x for x in ChatServer().get_messages()]
        self.assertEqual(True, False)-


if __name__ == '__main__':
    unittest.main()
