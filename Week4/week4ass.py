numb = [12, 75, 150, 180, 145, 525, 50]
n = []
for r in numb:
    while r < 500:
        if r > 150 and r <= 500:
            continue
        if r % 5 == 0:
            n.append(r)
        print(n)
