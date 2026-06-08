from song import Song


def reset():
    Song.reset()


def assert_eq(a, b, msg=None):
    if a != b:
        raise AssertionError(msg or f"{a!r} != {b!r}")


def test_initial_state():
    reset()
    assert_eq(Song.count, 0)
    assert_eq(Song.genres, [])
    assert_eq(Song.artists, [])
    assert_eq(Song.genre_count, {})
    assert_eq(Song.artists_count, {})


def test_creating_songs_updates_counts_and_lists():
    reset()
    Song('Shake It Off', 'Taylor Swift', 'Pop')
    assert_eq(Song.count, 1)
    assert 'Pop' in Song.genres
    assert 'Taylor Swift' in Song.artists
    assert_eq(Song.genre_count.get('Pop'), 1)
    assert_eq(Song.artists_count.get('Taylor Swift'), 1)

    Song('Blank Space', 'Taylor Swift', 'Pop')
    Song('Lose Yourself', 'Eminem', 'Rap')
    assert_eq(Song.count, 3)
    assert set(Song.genres) == {'Pop', 'Rap'}
    assert set(Song.artists) == {'Taylor Swift', 'Eminem'}
    assert_eq(Song.genre_count.get('Pop'), 2)
    assert_eq(Song.genre_count.get('Rap'), 1)
    assert_eq(Song.artists_count.get('Taylor Swift'), 2)
    assert_eq(Song.artists_count.get('Eminem'), 1)


def test_multiple_genres_and_artists():
    reset()
    Song('One', 'Artist A', 'Rock')
    Song('Two', 'Artist B', 'Rock')
    Song('Three', 'Artist A', 'Pop')
    assert_eq(Song.count, 3)
    assert set(Song.genres) == {'Rock', 'Pop'}
    assert set(Song.artists) == {'Artist A', 'Artist B'}
    assert_eq(Song.genre_count.get('Rock'), 2)
    assert_eq(Song.genre_count.get('Pop'), 1)
    assert_eq(Song.artists_count.get('Artist A'), 2)
    assert_eq(Song.artists_count.get('Artist B'), 1)


if __name__ == '__main__':
    test_initial_state()
    test_creating_songs_updates_counts_and_lists()
    test_multiple_genres_and_artists()
    print('OK')
