def add_query_string(url, query):
    """
    #var1
    que = []
    for k, v in query.items():
        que.append(k+'='+str(v))
    return url+'?'+'&'.join(que) if len(que)>0 else url"""
    # var2
    string = url+'?'
    for k, v in query.items():
        string += k+'='+str(v)+'&'
    return string.strip('&?')

print(add_query_string('pygen.ru', {'page': 1}))