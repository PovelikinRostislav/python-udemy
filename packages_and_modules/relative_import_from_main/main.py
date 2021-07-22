import unittest

class TestRelativeImport(unittest.TestCase):
    def test_relative_import(self):
        with self.assertRaises(ModuleNotFoundError):
            print(f"__name__ is {__name__}")
            print(f"__package__ is {__package__}")
            print("From main modules it's not allowed to use relative imports.")
            print("AFAIK, if __package__ is None, then relative imports are not allowed either, even if the __name__ is not __main__")
            from .module import foo

if __name__ == "__main__":
    unittest.main()

