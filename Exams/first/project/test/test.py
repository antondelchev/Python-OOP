from first.project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Explore")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Explore", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_init_with_empty_string_as_a_name(self):
        with self.assertRaises(ValueError) as msg:
            self.invalid_name = Library("")

        self.assertEqual("Name cannot be empty string!", str(msg.exception))

    def test_add_book_with_new_author_creates_empty_list(self):
        self.library.add_book("Author 1", "Title 1")
        result = self.library.books_by_authors

        self.assertEqual({"Author 1": ["Title 1"]}, result)

    def test_add_book_adds_a_new_title_to_an_existing_author(self):
        self.library.add_book("Author 1", "Title 1")
        self.library.add_book("Author 1", "Title 2")
        result = self.library.books_by_authors

        self.assertEqual({"Author 1": ["Title 1", "Title 2"]}, result)

    def test_add_new_reader(self):
        self.library.add_reader("Reader 1")
        self.assertEqual([], self.library.readers["Reader 1"])

    def test_add_reader_that_is_already_member_of_the_library(self):
        self.library.add_reader("Reader 1")
        result = self.library.add_reader("Reader 1")
        expected = f"Reader 1 is already registered in the {self.library.name} library."
        self.assertEqual(expected, result)

    def test_rent_book_with_nonexistent_reader(self):
        self.library.add_book("Author 1", "Title 1")
        result = self.library.rent_book("R1", "Author 1", "Title 1")
        expected = f"R1 is not registered in the {self.library.name} Library."
        self.assertEqual(expected, result)

    def test_rent_book_with_nonexistent_author(self):
        self.library.add_book("Author 1", "Title 1")
        self.library.add_reader("Reader 1")
        result = self.library.rent_book("Reader 1", "Author 2", "Title 1")
        expected = f"{self.library.name} Library does not have any Author 2's books."
        self.assertEqual(expected, result)

    def test_rent_book_with_nonexistent_title_by_existing_author(self):
        self.library.add_book("Author 1", "Title 1")
        self.library.add_reader("Reader 1")
        result = self.library.rent_book("Reader 1", "Author 1", "Title 2")
        expected = f"""{self.library.name} Library does not have Author 1's "Title 2"."""
        self.assertEqual(expected, result)

    def test_rent_book_successfully_and_removed_from_library(self):
        self.library.add_book("Author 1", "Title 1")
        self.library.add_reader("Reader 1")
        self.library.rent_book("Reader 1", "Author 1", "Title 1")
        result = self.library.readers
        expected = {"Reader 1": [{"Author 1": "Title 1"}]}
        self.assertEqual(expected, result)
        self.assertEqual({"Author 1": []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
