import json
from pprint import pprint


with open('movies.json', encoding='utf-8') as json_movies: # json 파일을 읽음
    json_data_1 = json.load(json_movies) # 읽은 json 파일을 저장한 후 커스터마이징 한 후 다시 내보내면 됨
    
with open('movies_add.json', encoding='utf-8') as json_movies_add:
    json_data_2 = json.load(json_movies_add)


moive_group = {}

moive_group['movies'] = json_data_1[0]
# pprint(json_data_1[0])
moive_group['movies_add'] = json_data_2[0]
# pprint(json_data_2[0])

# 커스터 마이징 한 json 파일 만들기
with open('trans.json', 'w', encoding='utf-8') as make_file:
    json.dump(moive_group, make_file, indent='\t')


# 만든 json 파일 읽기
with open('trans.json', encoding='UTF8') as json_trans:
    json_data_3 = json.load(json_trans)
    pprint(json_data_3)