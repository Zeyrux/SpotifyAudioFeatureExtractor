import pandas as pd
import numpy as np
from SpotifyAPI import SpotifyAPI, get_spotify_client_id_and_secret


playlists = [
    "https://open.spotify.com/playlist/2CH1YNKtf5UOT13VbCMpCw?si=7f54928eedb54246",
    "https://open.spotify.com/playlist/1jrTKl4l5KH8heNI6lvtkQ?si=70cb66a59faf4fac",
    "https://open.spotify.com/playlist/0WASrRrQGXY1mHCPwOwvwP?si=64539ca9bfeb4e5e",
    "https://open.spotify.com/playlist/3ZPfj74P3o6nNf2Gtun4bF?si=81e264afb50843c4",
    "https://open.spotify.com/playlist/4NQOlYTRwHTzgdge1U1Lk6?si=896769fdea13427d",
    "https://open.spotify.com/playlist/3cRnrwrFuUO2zR3PSk9KIF?si=399adc95829d4743",
    "https://open.spotify.com/playlist/14FnYwjinXHPqMSHd5GkQ2?si=97482d12fb9641f8",
    "https://open.spotify.com/playlist/64qoQvVzMulmln33wmzmPE?si=4a31b34e281c4073",
    "https://open.spotify.com/playlist/3hdlpbuqL69jh3rZu3dQa3?si=27c57c8f9efa4311",
    "https://open.spotify.com/playlist/2BlxPjY2Qe2WW42fpGMChb?si=dde655d744bc43ec",
    "https://open.spotify.com/playlist/1Afqg23mw4p2seXmmuQTx5?si=2e062b80251e4604",
    "https://open.spotify.com/playlist/4HpdOlvifFOH7lFTI3bLvc?si=5828b9e86d754498",
    "https://open.spotify.com/playlist/2Ff4Krdn1P4mfKIoRZZ2bw?si=e0613948a88741b6",
    "https://open.spotify.com/playlist/4B5ZOMy6vprm7QM8FeZTLq?si=3e9e17f416fa4bae",
    "https://open.spotify.com/playlist/32kTup9TLpDbJdTUiHX1Vs?si=df7e024810104826",
    "https://open.spotify.com/playlist/1tvqvzXVyVfZ6OLkAMHlK7?si=b7f56ae8ed924dce",
]


def main():
    api = SpotifyAPI(*get_spotify_client_id_and_secret())
    results = {}
    for playlist in playlists:
        data = api.get_playlist(playlist)

        for track in data.get_generator_tracks():
            print(track.get_name())
            result = api.get_features(track)

            results[track.get_name()] = result

    pd.DataFrame(results).to_csv("data.csv")


main()
