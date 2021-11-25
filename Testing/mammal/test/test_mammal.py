import unittest
from mammal.project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_mammal = Mammal("Thomas", "cat", "meow")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.test_mammal.name, "Thomas")
        self.assertEqual(self.test_mammal.type, "cat")
        self.assertEqual(self.test_mammal.sound, "meow")
        self.assertEqual(self.test_mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.test_mammal.make_sound(), "Thomas makes meow")

    def test_get_kingdom(self):
        self.assertEqual(self.test_mammal.get_kingdom(), self.test_mammal._Mammal__kingdom)

    def test_info(self):
        self.assertEqual(self.test_mammal.info(), "Thomas is of type cat")


if __name__ == "__name__":
    unittest.main()
