import requests
import json
from decouple import config
from pprint import pprint
TMDB_KEY = config('TMDB_KEY')
movies = []
for page_num in range(1, 4):
    # movie list
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_KEY}&language=ko-kr&page={page_num}'
    res = requests.get(URL).json()
    movie_list = res.get('results')
    for movie in movie_list:
        # pprint(movie)
        movie_obj = {}
        movie_obj['model'] = 'movies.movie'
        movie_obj['pk'] = movie.get('id')
        # movie credit
        # credit url
        movie_id = movie.get('id')
        cre_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_KEY}&language=ko'
        cre_res = requests.get(cre_URL).json()
        # pprint(cre_res)
        crew = cre_res.get('crew')
        for staff in crew:
            if staff['job'] == 'Director':
                direc_tmp = staff.get('name')
                break
        else:
            direc_tmp = ''
        movie_obj['fields'] = {
            'name': movie.get('title'),
            'genre_id': movie.get('genre_ids'),
            'user_rating': movie.get('vote_average'),
            'poster_url': movie.get('poster_path'),
            'description': movie.get('overview'),
            'director': direc_tmp,
            'like_users': []
        }
        movies.append(movie_obj)
with open('movies.json', 'w', encoding='utf-8') as make_files:
    json.dump(movies, make_files, ensure_ascii=False, indent="\t")