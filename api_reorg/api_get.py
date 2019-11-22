import requests
import json
from pprint import pprint

URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=f587667124773c74ca25857cae26ff82&language=ko-KR'
res = requests.get(URL).json()
genres_api = res.get('genres')
# pprint(res.get('genres')[0].get('name'))

genres = []
for genre in genres_api:
    genre_obj = {}
    genre_obj['id'] = genre.get('id')
    genre_obj['name'] = genre.get('name')
    genres.append(genre_obj)

# pprint(genres)
with open('genres.json', 'w', encoding='utf-8') as make_files:
    json.dump(genres, make_files, ensure_ascii=False, indent="\t")