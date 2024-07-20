#5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

import string
def print_rangoli(size):
    s1=list(string.ascii_lowercase)
    del s1[size:26]
    s1.reverse()
    n=2*(len(s1)+len(s1)-1)-1
    l1=[]
    l2=[]
    c=False
    for i in s1:
        l1.append(i)
        if c==True:
            l2=l1[::-1]
            l2.pop(0)
        c=True
        print(("-".join(l1+l2)).center(n,"-"))
    i1=s1
    i2=[]
    for j in range(size-1):
        i1.pop()
        i2=i1[::-1]
        i2.pop(0)
        print(("-".join(i1+i2)).center(n,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



# size=6
# s1=list(string.ascii_lowercase)
# s2=list(string.ascii_lowercase)
# del s1[size:26]
# # del s2[size:26]
# # s2.pop(0)
# s1.reverse()
# # super_list=s1+s2
# # print(super_list)
# n=2*(len(s1)+len(s1)-1)-1
# l1=[]
# l2=[]
# c=False
# for i in s1:
#     l1.append(i)
#     if c==True:
#         l2=l1[::-1]
#         l2.pop(0)
#     c=True
#     print(("-".join(l1+l2)).center(n,"-"))
#     # print(l1+l2)
#     # l2.app=end(j)
#     # print(("-".join(l1)+"-"+"-".join(l2)).center(2*(len(s1)+len(s2))-1,"-")
# i1=s1
# i2=[]
# for j in range(size-1):
#     i1.pop()
#     i2=i1[::-1]
#     i2.pop(0)
#     print(("-".join(i1+i2)).center(n,"-"))