letters = {4: 'К', 65: 'Щ', 12: 'П', 41: 'М', 36: 'У'}
remove_keys = [12, 65, 14, 37]
print({key:val for key, val in letters.items() if key not in remove_keys})