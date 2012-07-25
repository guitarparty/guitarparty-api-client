Guitarparty.com API client module
====================

Installation
------------

You can install this module using your package management method or choice, normally `easy_install` or `pip`. For example:

    pip install guitarparty

Authentication
------------

You need to obtain your API key from [Guitarparty.com](http://www.guitarparty.com/developers/api-key/), to do so you must be a registered user on the website.

To authenticate your requests, you can simply override the `api_key` property of the `guitarparty` module:

    import guitarparty
    guitarparty.API_KEY = 'your-api-key-here'

Usage
------------

    >>> songbooks = guitarparty.request('songbooks')
    >>> for songbook in songbooks:
    ...     print songbook['title']
    ...
    My first songbook

More detailed information about the API can be found on the [Guitarparty.com website](http://www.guitarparty.com/developers/api-docs/) 
