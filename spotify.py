import requests


def get_track_url(song_title):
    spotify_url = 'https://api.spotify.com/v1/search?access_token=BQCpqPYGSs6KZ17zk2Y_mItwsuLZjvpSef7sy-EW6zilKX4IoH5WNaezmfaG8b6cXsKXpvS6yJRsPNoTerikFtipikbbwq2iR-bJJDUopsIrgvdJLag_ep5lGunMRjDvp7p-2vtJglA4H_CbzZwojf7c0C0FEtPegA&refresh_token=AQD1yq7LK3JIBInM7Awv8KyHCheRSrDP8L170CgwB8q7fXZZxLYIq8YPb8-Fyw31mDGELuKv3inVTA7OQ5u7ItR7V7ULRwPEc6ep3wufB9lVF5Dot8x6bh_tr_b0fNLlVyw1KQ'
    params = {'q': song_title, 'type': 'track'}

    spotify_response = requests.get(spotify_url, params=params).json()
    #print(spotify_response)
    track_url = spotify_response['tracks']['items'][0]['preview_url']
    return track_url
