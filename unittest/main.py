import unittest

def foo():
    return 42

class TestFoo(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(foo(), 42)

if __name__ == '__main__':
    unittest.main()
