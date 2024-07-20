def wrapper(f):
    def fun(l):
        for i,j in zip(l,range(len(l))):
            l[j]=f"+91 {str(i)[-10:-5]} {(str(i)[-5:len(str(i))])}"
        return f(l) 
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 