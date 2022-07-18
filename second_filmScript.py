import tmdb3
import pandas as pd
import numpy as np
from tmdb3 import searchMovie


tmdb3.set_key('1c0676ede717a678562519363ae6d4f3')
tmdb3.set_cache('null')
tmdb3.set_locale('ru', 'ru')


headers = ['title','release', 'runtime','budget','revenue', 'lang', 'genre1', 'genre2',
           'country1','country2','actor1','actor2','actor3','actor4','actor5',
           'director','writer','studio1','studio2',
           'keyword1','keyword2','keyword3','keyword4','keyword5','keyword6','rating']

df_main = pd.read_excel('moviedb.xlsx')

#Проверка на пустоту и удаление первого столбца
if not(df_main.empty):
    df_main.drop(labels=["Unnamed: 0"], axis=1,inplace= True)

print(df_main)

df = []

#Добавление информации о фильме
def insert(data,info):
    try:
        info.append(data)
    except:
        info.append('0')

#Поиск фильма в базе данных tmdb
def find_film(tittle_film):
    return searchMovie(tittle_film)

#Сохранение информации в массив
def save_on_base(res):

    info=[]

    insert(res.title, info)
    insert(res.releasedate, info)
    insert(res.runtime, info)
    insert(res.budget if res.budget != 0 else np.nan, info)
    insert(res.revenue if res.revenue != 0 else np.nan, info)
    insert(res.languages[0].code if len(res.languages) > 0 else np.nan, info)
    insert(res.genres[0].name if len(res.genres) > 0 else np.nan, info)
    insert(res.genres[1].name if len(res.genres) > 1 else np.nan, info)
    insert(res.countries[0].code if len(res.countries) > 0 else np.nan, info)
    insert(res.countries[1].code if len(res.countries) > 1 else np.nan, info)
    insert(res.cast[0].name if len(res.cast) > 0 else np.nan, info)
    insert(res.cast[1].name if len(res.cast) > 1 else np.nan, info)
    insert(res.cast[2].name if len(res.cast) > 2 else np.nan, info)
    insert(res.cast[3].name if len(res.cast) > 3 else np.nan, info)
    insert(res.cast[4].name if len(res.cast) > 4 else np.nan, info)

    for person in res.crew:
        if person.job == 'Director':
            insert(person.name, info)
            break
    try:
        print(info[15])
    except IndexError:
        insert(np.nan, info)

    for person in res.crew:
        if person.job == 'Writer':
            insert(person.name, info)
            break
    try:
        print(info[16])
    except IndexError:
        insert(np.nan, info)

    insert(res.studios[0].name if len(res.studios) > 0 else np.nan, info)
    insert(res.studios[1].name if len(res.studios) > 1 else np.nan, info)
    insert(res.keywords[0].name if len(res.keywords) > 0 else np.nan, info)
    insert(res.keywords[1].name if len(res.keywords) > 1 else np.nan, info)
    insert(res.keywords[2].name if len(res.keywords) > 2 else np.nan, info)
    insert(res.keywords[3].name if len(res.keywords) > 3 else np.nan, info)
    insert(res.keywords[4].name if len(res.keywords) > 4 else np.nan, info)
    insert(res.keywords[5].name if len(res.keywords) > 5 else np.nan, info)
    insert(res.userrating, info)

    df.append(info)

    set = pd.DataFrame(df)

    set.columns = headers
    # Соединяю 2 dataframe в один и сохраняю в excel
    df_last = df_main.append(set,ignore_index=True)

    df_last= df_last.drop_duplicates(subset='title',keep='first')

    df_last= df_last.sort_values(by='title',ascending=True)

    df_last.to_excel('moviedb.xls')