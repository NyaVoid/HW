def all_variants(text):
    score = 1
    x = 0
    y = len(text)
    p = 1
    for i in range((len(text) * (1 + len(text))) // 2):
        if x == y:
            y -= 1
            x = 0
            score = 1 + p
            p += 1
        yield text[x:score]
        score += 1
        x += 1

a = all_variants("abc")
for i in a:
    print(i)
