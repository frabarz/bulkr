# -*- coding: utf-8 -*-

import configparser
from re import findall
from urllib.parse import urlencode

import requests

import base58

config = configparser.ConfigParser()
config.read('config.ini')
FLICKR = config['flickr']


class InvalidUrlError(Exception):
    pass

class FlickrApiError(Exception):
    pass


def rest_call(**kwargs):
    url = FLICKR['ENDPOINT']
    api_key = FLICKR['APIKEY']

    params = dict(api_key=api_key, format='json', nojsoncallback='1')
    kwargs.update(params)
    response = requests.get(url, params=kwargs)
    
    response.raise_for_status()
    
    root = response.json()
    if root.get('stat') == 'ok':
        return root
    else:
        message = root.get('message')
        raise FlickrApiError(message)


def parse_id(url):
    code = findall(r'flic\.kr\/p\/([1-9a-km-zA-HJ-NP-Z]+)', url)
    if code:
        return base58.decode(code[0])

    code = findall(r'flickr\.com\/photos\/[\w\-\@]+\/(\d+)', url)
    if code:
        return code[0]
    
    raise InvalidUrlError(url)


class Photo:
    def __init__(self, photo_id):
        self.photo_id = photo_id
        self.retrieve_info()

    def retrieve_info(self):
        root = rest_call(
            method='flickr.photos.getSizes',
            photo_id=self.photo_id)

        data = root.get('sizes')
        
        self.downloadable = data.get('candownload')
        self.embedable = data.get('canblog')
        self.printable = data.get('canprint')
        
        sizes = [PhotoSize(size) for size in data.get('size', [])]
        self.sizes = sorted(sizes, key=lambda s: s.area)
    
    def get_smallest(self):
        return self.sizes[0]
    
    def get_largest(self):
        return self.sizes[-1]

class PhotoSize:
    def __init__(self, root):
        self.width = int(root['width'])
        self.height = int(root['height'])
        self.label = root['label']
        self.source = root['source']
        self.media = root['media']

        self.square = (self.width == self.height)
        self.vertical = (self.height > self.width)
        self.area = self.width * self.height
        self.dimensions = '%dx%d' % (self.width, self.height)
