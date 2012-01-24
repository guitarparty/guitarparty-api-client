import requests
import logging

try:
    import json
except ImportError:
    import simplejson as json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

host = 'http://www.guitarparty.com'
api_endpoint = '/api/v2'
api_key = None


def deserialize(raw_data):
    data = json.loads(raw_data)
    if 'objects' in data.keys():
        return data['objects']
    else:
        return data



class Guitarparty(object):
    def __init__(self, api_key=None, host=None):
        _globals = globals()
        self.host = host or _globals['host']
        self.api_key = api_key or _globals['api_key']
        self.api_endpoint = api_endpoint or _globals['api_endpoint']
        self.url = '%s%s' % (self.host, self.api_endpoint)

    def get_songbooks(self):
        url = '%s/songbooks/' % (self.url)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def get_songbook(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def create_songbook(self, title, description=None, is_public=False):
        url = '%s/songbooks/' % (self.url)
        data = {
            'title': title,
            'description': description,
            'is_public': is_public,
        }
        r = self.make_request('post', url, data=json.dumps(data))
        return deserialize(r.content)

    def get_songbook_songs(self, sb_uri):
        url = '%s%ssongs/' % (self.host, sb_uri)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def get_songbook_songitem(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def delete_songbook(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request('delete', url)
        if r.status_code == 204:
            return True
        return False

    def make_request(self, method, uri, **kwargs):
        return requests.request(method, uri + '?api_key=' + self.api_key, **kwargs)


