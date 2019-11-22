# Django 서버

- 영화 DB(from TMDB) => REST API
- CSV
- HTML 또 Django => Vue =?

## api 정리

### 영화 장르

 https://api.themoviedb.org/3/genre/movie/list?api_key={key}&language=ko-KR 

### 인기 영화 리스트

- https://api.themoviedb.org/3/movie/popular?api_key={key}&language=ko-KR&page=1
- 변수: result(title, overview, id, vote_average, release_date, popularity, poster_path)

### 영화 디테일

- https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}&language=ko-KR
- genres[idx].name / overview / popularity / vote_average / title / runtime / poster_path / release_date

### 영화 크레딧(감독이름 얻기)

- https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={key}&language=ko-KR

### 영화 포스터

 https://image.tmdb.org/t/p/original/{poster_path}

=> API를 수집해서 다시 가공하기



# Vue Front

- 영화 리스트, 상세정보, 계정 프로필 
- plus alpha 새로운 기능(아직 미정)