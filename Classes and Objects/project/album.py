from project.song import Song


class Album:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs
        self.published = False

    def add_song(self, song: Song):
        pass

    def remove_song(self, song_name):
        pass

    def publish(self):
        pass

    def details(self):
        pass
