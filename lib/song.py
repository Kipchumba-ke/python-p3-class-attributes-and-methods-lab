class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count +=1
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_to_artist_count(artist)
        Song.add_to_genre_count(genre)
    #     Song.add_song_to_count(self)

    # @classmethod
    # def add_song_count(cls, count):
    #      cls.count += count
    # pass

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        pass

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        pass
