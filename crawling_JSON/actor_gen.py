import requests
import json
from decouple import config
from pprint import pprint
TMDB_KEY = config('TMDB_KEY')

with open('movies2.json', 'rt', encoding='UTF8') as f:
    jData = json.load(f)

actors = []
for movie_obj in jData:
    movie_id = movie_obj['pk']
    
    URL = f'http://api.themoviedb.org/3/movie/{movie_id}/casts?api_key={TMDB_KEY}'
    res = requests.get(URL).json()
    casts_list = res.get('cast')

    for i in range(5):
        try:
            actor_obj = {}
            actor_obj['model'] = 'movies.actor'
            actor_obj['pk'] = casts_list[i].get('id')    
            if not casts_list[i].get('profile_path'):
                profile_photo = []
            else:
                profile_photo = 'https://image.tmdb.org/t/p/original' + casts_list[i].get('profile_path')

            actor_obj['fields'] = {
            'movie_id': movie_id,
            'name': casts_list[i].get('name'),
            'character': casts_list[i].get('character'),
            'profile_photo': profile_photo
            }
            actors.append(actor_obj)
        except:
            break

with open('actors2.json', 'w', encoding='utf-8') as make_files:
    json.dump(actors, make_files, ensure_ascii=False, indent="\t")

