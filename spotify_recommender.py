import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from dotenv import load_dotenv
import os

load_dotenv()


class SpotifyRecommender:
    def __init__(self):

        client_id = os.getenv("CLIENT_ID")  # Replace with environment variable
        client_secret = os.getenv("CLIENT_SECRET")  # Replace with environment variable

        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Define emotion-to-genre mapping using valid Spotify genres
        self.emotion_mapping = {
            'Angry': {'genres': ['rock', 'metal']},
            'Disgust': {'genres': ['metal', 'industrial']},
            'Fear': {'genres': ['ambient', 'classical']},
            'Happy': {'genres': ['pop', 'dance']},
            'Sad': {'genres': ['blues', 'indie']},
            'Surprise': {'genres': ['edm', 'pop']},
            'Neutral': {'genres': ['indie', 'folk']}
        }

    def print_available_genres(self):
        try:
            genres = self.sp.recommendation_genre_seeds()
            print("Available genre seeds:")
            for genre in genres['genres']:
                print(genre)
        except Exception as e:
            print(f"Error retrieving genre seeds: {e}")

    def get_recommendation(self, emotion):
        if emotion not in self.emotion_mapping:
            emotion = 'Neutral'  # Fallback if unrecognized emotion

        genres = self.emotion_mapping[emotion]['genres']
        random.shuffle(genres)  # Shuffle genres to get different results

        for genre in genres:
            try:
                # Fetch multiple artists for variety
                search_results = self.sp.search(q=f'genre:{genre}', type='artist', limit=5)
                artists = search_results['artists']['items']

                if not artists:
                    continue

                # Pick a random artist
                artist_id = random.choice(artists)['id']

                # Get top tracks from the artist
                top_tracks = self.sp.artist_top_tracks(artist_id)['tracks']
                if not top_tracks:
                    continue

                # Filter tracks that have a preview
                preview_tracks = [track for track in top_tracks if track.get('preview_url')]

                if preview_tracks:
                    # Pick a random track that has a preview
                    track = random.choice(preview_tracks)
                else:
                    # If no track has a preview, pick any random track
                    track = random.choice(top_tracks)

                return {
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'url': track['external_urls'].get('spotify', ''),
                    'preview_url': track.get('preview_url', 'No preview available')
                }

            except spotipy.SpotifyException as e:
                print(f"Error with genre {genre}: {e}")
                continue  # Try the next genre in the list

        return {
            'name': 'No recommendation found',
            'artist': 'Try again later',
            'url': '',
            'preview_url': 'No preview available'
        }


# Example usage:
if __name__ == "__main__":
    recommender = SpotifyRecommender()
    emotion = input("Enter your emotion (Angry, Happy, Sad, etc.): ")
    song = recommender.get_recommendation(emotion)
    print(f"🎵 {song['name']} by {song['artist']}")
    print(f"🔗 Listen: {song['url']}")
