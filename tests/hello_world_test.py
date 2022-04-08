import unittest

from src.hello_world import hello_world


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")  # add assertion here


if __name__ == '__main__':
    unittest.main()
