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

        # call instance methods that update class-level trackers
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    def add_song_to_count(self):
        Song.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists_count(self):
        if self.artist in Song.artists_count:
            Song.artists_count[self.artist] += 1
        else:
            Song.artists_count[self.artist] = 1

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
