import random

 #main
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "Abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbol = "!@#$%^&*()_+<>?:{}"
 
 # inputing Username
Username = input ("Please Enter Your Username:")

 # adding
string = upper + lower + numbers +symbol 
length = 8

#printing
password = "".join(random.sample(string,length))
ready = input ("Are You Ready to See your Password: ")
if ready.lower() == 'no':
    print ("ok")
elif ready.lower() == 'yes':
    print ("Here is your password:",Username + password)
else:
 yesorno = input ("Type Yes Or No:")
 if yesorno.lower() == 'no':
    print ("ok")
 elif yesorno.lower() == 'yes':
   print ("Here is your password:",Username + password)