import re


buetFile = open("buet.txt")
ckruetFile = open("ckruet.txt", "r")
ckruetRead = ckruetFile.read()
commonfile = open(f'commonfile.txt', 'a')   # file to store common people
i = 1
for buetline in buetFile:
    name = buetline.strip()
    if not re.match("[a-z0-9]", name):
        if(name != "Name" and name != "Merit"):
            if name in ckruetRead:
                # print(f'{i}. {name}')
                # documenting in commonfile.txt
                commonfile.writelines(f'{i}. {name}\n')
                i = i+1

buetFile.close()
ckruetFile.close()
commonfile.close()
