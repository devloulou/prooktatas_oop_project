import requests
from params import API_KEY

# olyan base osztályt, amely megvalósítja a http requestek típusait
# lefejlesztünk egy movie search osztályt, ahol query-zni lehet title alapján a filmeket


class TMDBBase:

    urls = {}
    base_path = None

    version = 3
    def __init__(self):
        self.base_end_point = f"https://api.themoviedb.org/{self.version}"

    
    def _get_request(self, path, params=None):
        return self._request('GET', path, params=params) # itt kellene maga a requets hívás

    def _post_request(self, path, params=None, payload=None):
        return self._request('POST', path, params=params, payload=payload) # itt kell megadni a request hívást

    def _delete_request(self, path, params=None, payload=None):
        return self._request('DELETE', path, params=params, payload=payload) # itt kell megadni a request hívást

    def _request(self, method, path, params=None, payload=None):
        import json

        url = self._get_full_path(path)
        params = self._set_params(params)

        # api kulcs

        # if params is not None

        response = requests.request(
            method,
            url,
            params=params,
            data=json.dumps(payload) if payload else payload
        )

        return response.json()

    def _get_path(self, key):
        return f"{self.base_path}/{self.urls[key]}"

    def _get_full_path(self, path):
        return f"{self.base_end_point}/{path}"

    def _set_params(self, params):
        if not API_KEY:
            raise ValueError("You don't have API_KEY!")
        
        params_dict = {'api_key': API_KEY}

        if params:
            params.update(params_dict)
        else:
            params = params_dict
        
        return params
    

class Search(TMDBBase):

    urls = {
        "movie": "movie/"

    }

    base_path = "search"

    def __init__(self):
        super().__init__()
    
    def movie(self, **kwargs):
        path = self._get_path('movie')
        return self._get_request(path, kwargs)

if __name__ == "__main__":
    search = Search()

    data = search.movie(query="Alien")

    print(data['results'][0])