from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        pass

    def remove_album(self, album_name):
        pass

    def details(self):
        pass
