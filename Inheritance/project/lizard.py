from project.reptile import Reptile


class Lizard(Reptile):
    pass


lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
