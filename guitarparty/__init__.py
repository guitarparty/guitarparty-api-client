import requests

VERSION = '0.1'
URL = 'http://api.guitarparty.com/v2/%(resource)s/'
API_KEY = 'SECRET_API_KEY'

def request(resource, **params):
    options = {
        'headers': {
            'Guitarparty-Api-Key': API_KEY,
        },
    }
    options.update(params)
    r = requests.get(URL % {'resource': resource}, **options)
    return r.json
