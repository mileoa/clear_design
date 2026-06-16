def find_max(arr):
    # {I: i >= 1 и i < len(arr) и max_el = max(arr[:i])}
    if len(arr) == 0:
        return None
    i = 1
    max_el = arr[0]
    while i < len(arr):
        if arr[i] > max_el:
            max_el = arr[i]
        i += 1
    return max_el
