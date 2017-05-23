#C(N,K) = N! / (K! * (N-K)!)

def fact(a):
    f = 1
    for i in range(a):
        f = f * i
    return f

def cnk(n, k):
    n_fact = fact(n)
    k_fact = fact(k)
    nk_fact = fact(n - k)
    return n_fact/(k_fact*nk_fact)

n = int(input('N:'))
k = int(input('K:'))

print(cnk(n, k))
