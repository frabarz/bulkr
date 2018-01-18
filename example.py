#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flickr import FlickrApiError, InvalidUrlError, Photo, parse_id

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line in file:
            url = line.strip()
            try:
                flickr_id = parse_id(url)
                photo = Photo(flickr_id)
                large = photo.get_largest()
                output = 'wget %s' % large.source
            except InvalidUrlError:
                output = '# Not a valid URL: %s' % url
            except FlickrApiError as err:
                output = '# %s | Flickr API error: %s' % (url, err)

            print(output)
