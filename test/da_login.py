# **********************************************************
# da_login.py
#******************************************

import time
modulename = raw_input("Enter [[Appname]] you wish to execute ").lower()
time.sleep(2)
#print("You have enter: => {} App! Are you sure you want to proceed? : ".format(modulename))
entered=("You have enter: => {} App! Are you sure you want to proceed? : ".format(modulename))
found=("Importing Your module: =>:  {} : Loading the application {}!".format(modulename, modulename))
if modulename:
    print(entered)
answer = None
while answer not in ("yes", "no"):
    answer = raw_input("Enter [yes] or [no]to proceed: ").lower()
    if answer == "yes":
        #print("Importing Your module: =>:  {} App!".format(modulename))
        try:
            if modulename == 'bdgc':
                print(found)
                import  Bdgc_prod_login                                                                                       
            elif modulename == "nac3":
                import Nac3_prod_login
            elif modulename == "case":
                import Casemgmnt_prod_login
            elif modulename == "cove":
                import Covepoint_prod_login
        except Exception as ss:
            print('Sorry Nosuch module: msg {} '.format(ss))
###################################################
