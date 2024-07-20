if __name__ == '__main__':
    s = input()
    b=False
    for i in s:
        if i.isalnum()==True:
            b=True
            break
    print(b)
    l=[str.isalpha, str.isdigit, str.islower, str.isupper]
    for i in l:
        a=False
        for j in s:
            if i(j)==True:
                a=True
                break
        print(a)
