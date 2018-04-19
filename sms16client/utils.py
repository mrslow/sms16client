from nested_lookup import nested_lookup

def find(key, value):
    error = nested_lookup(key, value)
    return error[0] if error and error[0] != "0" else None
