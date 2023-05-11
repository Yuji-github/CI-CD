import unittest
import logging


class MyTestCase(unittest.TestCase):
    def test_something(self):
        logging.info('......Testing......')
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()