import collections
f = open("dictonary.txt","r")
temp=f.readlines()
message_l = "hi this is this this assassdd is"
message_u= message_l.upper()
message = message_u.split()
found=[]
not_found=[]
temp = [k.replace('\n', '') for k in temp]
for i in temp:
    for j in message:
        if str(j)==str(i):
            found.append(j)
        else:
            if j not in not_found:
                not_found.append(j)

not_found =[m for m in not_found if m not in found]
print("--------------------------------------------------------------------------------------------------")
print("found elements are : ",found)
print("--------------------------------------------------------------------------------------------------")
counter=collections.Counter(found)
print("found elements with frequency: ",counter)
print("--------------------------------------------------------------------------------------------------")
print("not found elements are : ",not_found)
print("--------------------------------------------------------------------------------------------------")
f.close()


