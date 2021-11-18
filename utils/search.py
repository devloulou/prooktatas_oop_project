# van egy listán, amiben .mkv file-ok vannak
# ezekhez a file-okhoz akarunk letölteni 
    # képeket
    # szöveges állományt -> json
    # még egyéb metaadatokat
    # ha mégiscsak a listában van az elem, akkor próbáljuk megtalálni a megfelelőt


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
            response = search.movie(query=movie_name)['results'][0]
        except Exception as e:
            return False, str(e)

        return response

    def get_posters(self):
        pass

    def get_poster_link(self):
        pass
        #return 

    def write_image(self):
        pass


if __name__ == '__main__':
    test = Search()

    print(test.image_path_string)

    data = test.get_json_data('Alien')

    print(data)