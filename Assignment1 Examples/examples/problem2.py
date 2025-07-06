class Tracklist:
    _songs = []

    def __init__(self, album):
        self._album = album

    def add(self, song):
        self._songs.append(song)

    def get_all(self):
        return self._songs