

def info_kwargs(**kwargs):
    list_of_keys = sorted(list(kwargs.keys()))
    for key in list_of_keys:
        print(f'{key}: {kwargs[key]}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
info_kwargs(city='Perm', name='Tony', height=175)