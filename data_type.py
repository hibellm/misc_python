

# MANIPULATE DATA TYPES

# LIST
list=[['ABC1234'],['DEF4567'],['XYZ9876']]
print(f'List :{str(list)}')

#FLATTEN LIST
flat_list = [item for sublist in list for item in sublist]
print('Flat List :'+str(flat_list))

match='DEF4567'

#LOOP THROUGH LIST
for l in list:
    print(l)  #THE ENTRIES ARE A LIST

for l in list:
    if match == l[0]:
        print(str(l[0])+' Matched :0)!') #THE ENTRIES ARE A STR
    else:
        print(str(l[0])+' Not matched :0(')



for l in flat_list:
    print(l) #THE ENTRIES ARE A STR


for l in flat_list:
    if match == l:
        print(l+' Matched :0)!') #THE ENTRIES ARE A STR
    else:
        print(l+' Not matched :0(')

