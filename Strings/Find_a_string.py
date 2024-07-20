# def count_substring(string, sub_string):
#     coun=0
#     s=False
#     for j in range(len(string)-1):
#         if sub_string[0]==string[j]:
#             g=j
#             for n in range(1,len(sub_string)):
#                 g=g+1
#                 if string[g]==sub_string[n]:
#                     s=True
#                 else: s=False
#             g=0
#             if s==True:
#                 coun=coun+1
#     return coun
def count_substring(string, sub_string):
    
    return
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)