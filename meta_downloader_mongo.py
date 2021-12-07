import os
import json
from utils.file_handler import FileHandler
from utils.search import Search
from utils.mongo_handler import MongoHandler


def download_metadata():
    # ha nincsenek metaadatok, akkor töltsük le őket
    search = Search()
    db = MongoHandler()
    file_handler = FileHandler()

    # az összes adatot , teljes egészében lekérjük -> ezt majd refaktorálni kellene
    poster_list = file_handler.get_poster_list()

    movies = [movie['search_name'] for movie in db.get_documents({})]
    poster_path = [{movie['search_name']: movie['poster_path']} for movie in db.get_documents({})]

    for item in movies:
        if item not in poster_list:
            for poster in poster_path:
                if list(poster.keys())[0] == item:
                    data = {"poster_path": list(poster.values())[0] }
                    search.movie_name = item
                    search.write_image(data)
                    print(item)

    for movie in file_handler.get_movie_list():
        # database_movies[movie] -> ez a poster_path értékét adja vissza

        if movie not in movies:
            data = search.get_json_data(movie)
            data['search_name'] = movie
            poster_path = search.write_image(data)

            print(poster_path)

            if poster_path:
                data['poster_file_path'] = poster_path

            db.insert_document(data)
    # diff = search.file_handler.get_diff() # ez a logika itt nem használható

    # print(diff)

    # if diff["need_to_download_meta"]:
    #     for item in diff["need_to_download_meta"]:
    #         data = search.get_json_data(item)
    #         # itt változtatni kell -> nem kiírjuk, hanem " betöltjük a db-be"
    #         # utólag updateljük
    #         db.insert_document(data)


    # ha lekérjük az adatokat, akkor
    # a json-t a db-be kell betölteni
    # mielőtt betöltjük, a json-höz hozzá kellene adni a json-höz tartozó poster elérési útját



if __name__ == '__main__':
    db = MongoHandler()
    download_metadata()