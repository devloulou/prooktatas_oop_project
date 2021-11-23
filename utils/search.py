# van egy listán, amiben .mkv file-ok vannak
# ezekhez a file-okhoz akarunk letölteni 
    # képeket -> pipa
    # szöveges állományt -> json -> pipa
    # még egyéb metaadatokat
    # ha mégiscsak a listában van az elem, akkor próbáljuk megtalálni a megfelelőt
# később refakotorálnoi fogjuk a kódot: python loggert fogunk használni

import tmdbsimple as tmdb
from urllib.request import urlopen

class Search:
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'
    image_path_string = 'https://image.tmdb.org/t/p/original'
    backdrop_path_string = 'https://image.tmdb.org/t/p/original'

    def __init__(self):
        pass

    def get_json_data(self, movie_name):
        if not movie_name:
            raise Exception("Nem adtál meg film címet, kérlek pótold")
        try:
            search = tmdb.Search()
            response = search.movie(query=movie_name)['results']

        except Exception as e:
            return False, str(e)

        return response[0] if response else False

    def _get_poster_link(self, data):
        return f"{self.image_path_string}{data['poster_path']}"
        
    def write_image(self, data, movie_name):
        if not data:
            return False, "There is no data"

        poster_link = self._get_poster_link(data)

        try:
            with open(movie_name + '.jpg', "wb") as poster:
                poster.write(urlopen(poster_link).read())
        except Exception as e:
            return False, str(e)


if __name__ == '__main__':
    test = Search()

    #print(test.image_path_string)

    movie_name = 'Braveheart'

    data = test.get_json_data(movie_name)

    print(data)

    if not data:
        print(f"error at query data from api: {data}")
        exit()

    test.write_image(data, movie_name)

    