strind="""hi  how  are     what  ar e     you   do ing"""
newstring=""
for inde,char in enumerate(strind):
    if not(strind[inde]==" " and strind[inde+1]==" "):
        newstring= newstring+char
print(newstring)    