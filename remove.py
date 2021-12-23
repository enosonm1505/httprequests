a=open('a.txt','r')
c=a.readlines()
for i in c:
    foo = i[:-4]
    print(foo)
    d=open("c.txt","a")
    d.write(foo+"\n")
    d.close