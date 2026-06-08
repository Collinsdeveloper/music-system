import pytest

from song import Song


def setup_function():
    # reset class state before each test
    Song.reset()


def test_initial_state():
    assert Song.count == 0
    assert Song.genres == []
    assert Song.artists == []
    assert Song.genre_count == {}
    assert Song.artists_count == {}


def test_creating_songs_updates_counts_and_lists():
    s1 = Song('Shake It Off', 'Taylor Swift', 'Pop')
    assert Song.count == 1
    assert 'Pop' in Song.genres
    assert 'Taylor Swift' in Song.artists
    assert Song.genre_count['Pop'] == 1
    assert Song.artists_count['Taylor Swift'] == 1

    s2 = Song('Blank Space', 'Taylor Swift', 'Pop')
    s3 = Song('Lose Yourself', 'Eminem', 'Rap')

    assert Song.count == 3
    # genres unique
    assert set(Song.genres) == {'Pop', 'Rap'}
    # artists unique
    assert set(Song.artists) == {'Taylor Swift', 'Eminem'}

    assert Song.genre_count['Pop'] == 2
    assert Song.genre_count['Rap'] == 1

    assert Song.artists_count['Taylor Swift'] == 2
    assert Song.artists_count['Eminem'] == 1


def test_multiple_genres_and_artists():
    Song('One', 'Artist A', 'Rock')
    Song('Two', 'Artist B', 'Rock')
    Song('Three', 'Artist A', 'Pop')

    assert Song.count == 3
    assert set(Song.genres) == {'Rock', 'Pop'}
    assert set(Song.artists) == {'Artist A', 'Artist B'}
    assert Song.genre_count['Rock'] == 2
    assert Song.genre_count['Pop'] == 1
    assert Song.artists_count['Artist A'] == 2
    assert Song.artists_count['Artist B'] == 1
