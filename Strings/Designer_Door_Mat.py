s=input()
lis=s.split(" ")
l=int(lis[0])
w=int(lis[1])
for i,j in zip(range(((w-3)//2),0,-3),range(1,((w-6)//3)+1,2)):
    print(i*"-"+j*".|."+i*"-")
print(((w-7)//2)*"-"+"WELCOME"+((w-7)//2)*"-")
for k,l in zip(range(3,((w-3)//2)+1,3),range(((w-6)//3),-1,-2)):
    print(k*"-"+l*".|."+k*"-")
