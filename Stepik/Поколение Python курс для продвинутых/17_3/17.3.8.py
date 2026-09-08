with open(input(), encoding='utf-8') as f:
    countr_pop = f.readlines()

for line in countr_pop:
    line = line.strip().split('\t')
    countr = line[0]
    pop = line[1]
    if countr[0] == 'G' and int(pop) > 500000:
        print(countr)