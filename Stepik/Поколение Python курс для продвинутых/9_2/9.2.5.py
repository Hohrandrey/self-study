f = set(input().split()).intersection(set(input().split()))
print(' '.join(sorted(f, reverse=True, key=int)) if len(f)!=0 else "BAD DAY")