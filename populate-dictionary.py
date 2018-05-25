# Complete the function so that it takes an array of keys and a default value and returns a hash (Ruby) / dictionary (Python) 
# with all keys set to the default value.

# Example
# ["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}

def populate_dict(keys, default):
    my_dict = {}
    for key in keys:
        my_dict[key] = default
    return my_dict
    
# Another shorher solution using comprehension is

def populate_dict(keys, default):
    return {key: default for key in keys}
    
# Another solution using fromkeys is

def populate_dict(keys, default):
    return dict.fromkeys(keys, default)
