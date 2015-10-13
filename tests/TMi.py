__author__ = 'beyzanurkocak'

import unittest
from main import PMi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(PMi.size_list([]),0)


if __name__ == '__main__':
    unittest.main()

