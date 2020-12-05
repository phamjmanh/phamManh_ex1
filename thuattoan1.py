if __name__ == '__main__':
    L = '123456789'
    a = []
    for i in L:
        a.append(['+%s' % i, '-%s' % i, '%s' % i])
    def permute(list, s):
        if list == 1:
            return s
        else:
            return [y + x
                    for y in permute(1, s)
                    for x in permute(list - 1, s)
                    ]
    b=permute(9, ["0", "1", "2"])
    for i in range(len(b)):
        List_1 = []
        c = b[i]
        for j in range(len(c)):
            d = int(c[j])
            g = a[j][d]
            List_1.append(g)
        d = ''.join(map(str, List_1))
        if d[0] != '+':
            e = eval(d)
            if e == 100:
                e = ''.join(map(str, List_1))
                print(e)
