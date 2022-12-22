def frequencySort(s: str) -> str:

    l = [ord(i) for i in s]
    k = [chr(i) for i in sorted(l)]
    d = {}
    for i in sorted(l):
        try:
            d[i] += 1
        except:
            d[i] = 1

    n = list()
    f = sorted(d.values(), reverse=True)

    while len(d) > 0:
        for i in d:
            # print("d: {} | f: {}".format(d[i], f[0]))
            if d[i] == f[0]:
                for j in range(0, f[0]):
                    n.append(i)
                del d[i]
                del f[0]
                break

    z = [chr(x) for x in n]
    return ''.join(z)

print(frequencySort('CbaabAC'))
print(frequencySort('tree'))