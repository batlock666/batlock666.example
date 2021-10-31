# NOQA: D100

import unittest

from batlock666.example import hello


class HelloTest(unittest.TestCase):  # NOQA: D101
    """Tests for function ``hello``.
    """

    def test_hello_without_name(self):  # NOQA: D102
        """Test function ``hello`` without a name.
        """
        self.assertEqual(hello(), "Hello, World!")

    def test_hello_with_name(self):  # NOQA: D102
        """Test function ``hello`` with a name.
        """
        self.assertEqual(hello("Joe"), "Hello, Joe!")


if __name__ == "__main__":
    unittest.main()
