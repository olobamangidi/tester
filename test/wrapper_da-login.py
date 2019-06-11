#****************************************************
# wrapper_da-login.py
# program to execute module 
####################################################
import sys
sys.path.append("C:\Python27\da-testing-login-python\scripts")

try:
	print("Loging into prod_da documentum")
	import prod_da_modules
	print("End ... thanks for using this program")
except Exception as rr:
    print('Sorry Nosuch module: msg {} '.format(rr))
