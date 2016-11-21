#coding: utf-8

from nested_lookup import nested_lookup

def find(key, obj):
    match = nested_lookup(key, obj)
    return match[0] if len(match) > 0 else None
