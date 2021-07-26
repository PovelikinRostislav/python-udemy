import unittest

def return_42():
    return 42

def raise_exception():
    raise Exception("This is exception!")

class TestUnittest(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(return_42(), 42)

    def test_assert_true(self):
        boolean_list = [False, False, True]
        self.assertTrue(any(boolean_list))

    def test_assert_false(self):
        boolean_list = [True, True, True, False]
        self.assertFalse(all(boolean_list))

    def test_assert_raises(self):
        with self.assertRaises(Exception):
            raise_exception()

if __name__ == '__main__':
    unittest.main()
