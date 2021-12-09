from project_third.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        for el in self.decorations:
            if el.__class__.__name__ == decoration.__class__.__name__:
                self.decorations.remove(el)
                return True

        return False

    def find_by_type(self, decoration_type: str):
        for el in self.decorations:
            if el.__class__.__name__ == decoration_type:
                return el

        return "None"
