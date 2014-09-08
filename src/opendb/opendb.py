import requests
import json
from urllib.parse import urlparse, urlunparse, urljoin

def urljoin(*args):
    """
    Joins given arguments into a url. Trailing but not leading slashes are
    stripped for each argument.
    """

    return "/".join(map(lambda x: str(x).rstrip('/'), args))

class OpenDB(object):

    def __init__(self, address='http://opendb.netfluid.org/'):
        self.address = address

    def login(username, password):
        pass

    def get_json_response(self, path):
        url = urljoin(self.address, path)
        response = requests.get(url)
        response.encoding = 'utf-8-sig'

        return response.json()

    def post(self, path, params):
        url = urljoin(self.address, path)
        response = requests.post(url, params=params)
        response.encoding = 'utf-8-sig'

        return response.json()

    def put(self, path, params):
        url = urljoin(self.address, path)
        response = requests.post(url, params=params)
        response.encoding = 'utf-8-sig'

        return response.json()

    def request_delete(self, path):
        url = urljoin(self.address, path)
        response = requests.delete(url)
        response.encoding = 'utf-8-sig'

        return response.json()

    def collections(self):
        return self.get_json_response(urljoin('rest'))

    def items(self, collection):
        return self.get_json_response(urljoin('rest', collection))

    def item(self, collection, id):
        return self.get_json_response(urljoin('rest', collection, id))

    def add(self, collection, id, item):
        return self.post(urljoin('rest', collection, id), params=item)

    def update(self, collection, id, item):
        return self.put(urljoin('rest', collection, id), params=item)

    def delete(self, collection, id):
        return self.request_delete(urljoin('rest', collection, id))
