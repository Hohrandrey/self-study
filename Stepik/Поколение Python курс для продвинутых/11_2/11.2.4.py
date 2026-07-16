def build_query_string(dic):
    return '&'.join(f'{elem}={dic[elem]}' for elem in sorted(dic))

print(build_query_string({'name': 'timur', 'age': 28}))