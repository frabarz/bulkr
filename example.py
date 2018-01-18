#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flickr import Photo, parse_id

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line in file:
            url = line.strip()
            try:
                flickr_id = parse_id(url)
                photo = Photo(flickr_id)
                large_url = photo.get_largest()
                output = '%s\t%s' % (line, large_url)
            except:
                output = url

            print(output)
