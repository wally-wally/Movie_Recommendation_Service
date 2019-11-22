import requests
import json
from decouple import config
from pprint import pprint

TMDB_KEY = config('TMDB_KEY')

URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_KEY}&language=ko-KR'
res = requests.get(URL).json()
genres_api = res.get('genres')
# pprint(res.get('genres')[0].get('name'))

genres = []
for genre in genres_api:
    genre_obj = {}
    genre_obj['model'] = 'movies.genre'
    genre_obj['pk'] = genre.get('id')
    genre_obj['fields'] = {
        'name': genre.get('name')
    }
    genres.append(genre_obj)

# pprint(genres)
with open('genres.json', 'w', encoding='utf-8') as make_files:
    json.dump(genres, make_files, ensure_ascii=False, indent="\t")
