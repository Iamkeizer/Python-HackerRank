def mutate_string(string, position, character):
    a=""
    for j,n in zip(s,range(len(s))):
        if n==int(i):
            a=a+c
        else: a=a+j
    return a

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)