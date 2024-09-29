def access_nested_map(nested_map, path):
    """
    Access a nested map using a list of keys or indices.
    
    Parameters:
    - nested_map: dict or list
    - path: list of keys/indices to navigate through the nested map
    
    Returns:
    - The value at the end of the path
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map


data = {
    'user': {
        'profile': {
            'name': 'Aya',
            'age': 30
        }
    }
}

path = ['user', 'profile', 'name']
print(access_nested_map(data, path))  # Output: Aya
