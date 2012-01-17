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
    guitarparty.api_key = 'your-api-key-here'
    GP = guitarparty.Guitarparty()

You can also pass your API key to the Guitarparty object on initialization

    import guitarparty
    GP = guitarparty.Guitarparty(api_key='your-api-key-here')

Usage
------------

    >>> GP = guitarparty.Guitarparty()
    >>> GP.create_songbook('My first songbook')
    >>> for songbook in GP.get_songbooks():
    ...     print songbook.title
    ...
    My first songbook

API methods
------------

* ``Guitarparty``.`get_songbooks`

More detailed information about the API can be found on the [Guitarparty.com website](http://www.guitarparty.com/developers/api-docs/) 
