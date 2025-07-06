class Tracklist:
    """
    A class representing a tracklist for an album.
    Each instance maintains its own private list of songs.
    """
    def __init__(self, album_name):
        """
        Initialize a Tracklist with an album name and empty song list.
        
        Args:
            album_name (str): Name of the album
        """
        self._album_name = album_name
        self._songs = []  # Instance variable for each instance

    def add(self, song):
        """
        Add a song to the tracklist.
        
        Args:
            song (str): Name of the song to add
        """
        self._songs.append(song)

    def get_all(self):
        """
        Get all songs in the tracklist.
        
        Returns:
            list: List of all songs in the tracklist
        """
        return self._songs
