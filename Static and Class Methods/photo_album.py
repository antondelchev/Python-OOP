import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        total_pages = math.ceil(photos_count / 4)
        return cls(total_pages)

    def add_photo(self, label):
        added = False
        page_number, slot_number = (0, 0)
        for page in range(len(self.photos)):
            if not self.photos[page]:
                self.photos[page] = [[], [], [], []]
            for slot in range(4):
                if not self.photos[page][slot]:
                    self.photos[page][slot] = label
                    page_number, slot_number = (page, slot)
                    added = True
                    break
            if added:
                break

        if added:
            return f"{label} photo added successfully on page {page_number + 1} slot {slot_number + 1}"
        else:
            return "No more free slots"

    def display(self):
        result = "-" * 11

        for page in range(len(self.photos)):
            result += "\n"
            for photo in range(len(self.photos[page])):
                if not self.photos[page][photo] == []:
                    result += "[] "
            result += "\n"
            result += "-" * 11

        return result
