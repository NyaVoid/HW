def introspection_info(obj):
    b = []
    a = []
    aa = list(str(type(1)))
    aa = aa[aa.index("'"):aa.index('>')]
    ab = ''
    for i in aa:
        ab += i
    for i in dir(obj):
        if '_' in list(i) != True:
            b.append(i)
        else:
            a.append(i)
    c = [ab.split("'")[1], a, b, __name__]
    res = {'type': c[0], 'attr': c[1], 'methods': c[2], 'module': c[3]}
    return res
print(introspection_info(1))
