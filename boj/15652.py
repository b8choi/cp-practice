n, m = input().split()
n = int(n)
m = int(m)

def perm(seq):
    if len(seq) == m:
        for i in seq:
            print(i, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if len(seq) == 0 or i >= seq[-1]:
                perm(seq + [i])

perm([])
