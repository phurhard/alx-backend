#!/usr/bin/env python3
""" A simple helper function to facilitate pagination"""


def index_range(page, page_size):
    """ This function returns a tuple of the range of in
    dexes given a page number amd page size"""
    start_index = (page_size * page) - page_size
    end_index = page_size * page
    return (start_index, end_index)
