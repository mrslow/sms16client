from nested_lookup import nested_lookup

def find(key, source):
    value = nested_lookup(key, source)
    return value[0] if value and value[0] != "0" else None
