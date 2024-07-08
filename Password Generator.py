def add():
   user=input("Account_user: ")
   passw=input("password: ")
   with open("password.txt","a") as f:
       f.write(user +"|"+ passw+"\n")

def view():
  with open("password.txt","r") as f:
   for line in f.readlines():
       data=line.rstrip()
       user,passw = data.split("|")
       print("User: ",user,", Password: ",passw)


msg=input("Would you like to change you password or wanted to read the password(add/view):  ")
if msg=="add":
   add()
elif msg=="view":
   view()
else:
  print("Bye")