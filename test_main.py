import unittest
from main import get_greeting

class TestMain(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(get_greeting(), "Hello, DevOps! Lab 2 CI is working.")

if __name__ == "__main__":
    unittest.main()