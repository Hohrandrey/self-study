emails = {
    'gmail.com': ['johnny', 'monkey-man'],
    'hotmail.com': ['chani'],
    'yandex.ru': ['petrpn', 'rtgxv5dsfsd4'],
}

res = []
for name, emails in emails.items():
    for email in emails:
        res.append(email+'@'+name)
print(*sorted(res), sep='\n')