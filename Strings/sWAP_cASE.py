def swap_case(s):
    a=""
    for i in s:
        if i==(i.upper()):
            i=i.lower()
            a+=i
        elif i==(i.lower()):
            i=i.upper()
            a+=i
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)