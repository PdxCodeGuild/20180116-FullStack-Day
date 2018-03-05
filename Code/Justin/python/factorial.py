def fact(n, depth):
    print('\t'*depth, f'factorial {n}')
    if n == 1:
        print('\t'*depth, n, depth)
        return n
    else:
        print('\t'*depth, n, depth)
        return n*fact(n-1, depth + 1)

print(fact(10, 0))