def buggy_function_3(items):
    items.append('new')
    return items # Mutates default list