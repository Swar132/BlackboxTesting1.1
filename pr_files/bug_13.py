def buggy_function_12():
    # No error handling
    data = requests.get('https://api.example.com/data')
    return data.json()