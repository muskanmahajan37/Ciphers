import numpy as np

def convert_list(word):
    return list(word)


m=message.replace(" ","#")

key=4
col=len(message)

rem=col%key

quo=col//key
if(rem!=0):
    quo=quo+1
else:
    quo=quo

n=convert_list(m)
add_zero=(quo*key)-col

for i in range(0,add_zero):
    n.append(0)

np.array(n)
o=np.reshape(n,(quo,key))
p=o.transpose()
b= " "
for k in range(0,p.shape[0]):
    for l in range(0,p.shape[1]-1):
        b+=str(p[k,l])
    b+=str(p[k,-1])
res_1=b.replace("#"," ")
res_2=res_1.replace("0"," ")
print(res_2)

