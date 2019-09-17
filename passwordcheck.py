import re

passw =  input('enter possible passwords: \n')
pass_list = passw.split(',')

for passwords in pass_list:
    m = re.search( "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$",passwords)
    print(m)
    if(m!=None):
        print(passwords ,'Not acceptable')
    else:
        print(passwords ,' Not acceptable')