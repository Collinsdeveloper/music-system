class Song:
    """Song class that tracks global song statistics.

    Instance attributes
    - name, artist, genre

    Class attributes
    - count: total Song instances
    - genres: unique genres list
    - artists: unique artists list
    - genre_count: dict mapping genre -> count
    - artists_count: dict mapping artist -> count
    """

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # call class methods that update class-level trackers
        type(self).add_song_to_count()
        type(self).add_to_genres(self.genre)
        type(self).add_to_artists(self.artist)
        type(self).add_to_genre_count(self.genre)
        type(self).add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

    @classmethod
    def reset(cls):
        """Reset all class-level trackers. Useful for tests."""
        cls.count = 0
        cls.genres = []
        cls.artists = []
        cls.genre_count = {}
        cls.artists_count = {}

    def __repr__(self):
        return f"<Song name={self.name!r} artist={self.artist!r} genre={self.genre!r}>"
