def get_key(val):
    for key, value in ref.items():
         if val == value:
             return key
def get_val(kee):
    for key, value in ref.items():
         if key == kee:
             return value
ref = {1: 'A', 2: 'B', 3: 'C',
       4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L'
          ,13:'M',14:'N',15:'O',16:'P',17:'Q'
          ,18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X'
          ,25:'Y',26:'Z'}

message="GUVF VF ZL FRPERG ZRFFNTR"
shift_new=1
translator= " "
a=" "
b=" "
while(shift_new<26):
    k=len(message)-1
    i=0
    while i<=k:
        if (message[i] == " "):
            translator = translator + " "
        elif (message[i] == "!"):
            translator = translator + "!"
        elif (message[i] == ","):
            translator = translator + ","
        elif (message[i] == "."):
            translator = translator + "."
        elif (message[i] == ";"):
            translator = translator + ";"
        elif (message[i] == "-"):
            translator = translator + "-"
        elif (message[i] == "_"):
            translator = translator + "_"
        else:
            l=message[i]
            j=get_key(l.upper())
            next_1=int(j)+int(shift_new)
            next=next_1%26
            if(next == 0):
                m=get_val(int(26))
            else:
                m=get_val(int(next))
            translator = translator + str(m)
        i=i+1
    for p in range(len(message)):
        if(message[p] == message[p].lower()):
            print(translator[p+1].lower(),end='')
        else:
            print(translator[p+1].upper(),end='')
    shift_new=shift_new+1
    translator=" "
    print("\n")

