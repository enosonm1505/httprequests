import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

a=open("c.txt","r")
c=a.readlines()
for i in c:
    cd=i
    ac=cd.rstrip()
    r = requests.get("https://"+ac+"/")
    if '200' in r.content:       
        print('200'+i)
        acd=open("output.txt","a")
        acd.write("\n")
        acd.write("\n")
        acd.write("\n")
        acd.write("Hostname : "+i)
        acd.write("\n")
        acd.write("\n")
        acd.write(r.content)
    elif '302' in r.content:
        print('200'+i)
        acd=open("output.txt","a")
        acd.write("\n")
        acd.write("\n")
        acd.write("\n")
        acd.write("Hostname : "+i)
        acd.write("\n")
        acd.write("\n")
        acd.write(r.content)
    else:
        print("something wrong")