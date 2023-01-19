def Naopako(s):
    novi=" "
    for znak in s:
        novi=znak+novi
    return novi

s=input()
nova = Naopako(s)+s
print(nova)