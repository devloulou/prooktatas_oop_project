import requests

API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

get_movie_request = "https://api.themoviedb.org/3/search/movie?api_key=454b6ca4172e455fe7a7d8395c10d6d9&query=Alien"

r = requests.get(get_movie_request)

print(r.content)