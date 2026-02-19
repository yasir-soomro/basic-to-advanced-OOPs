
print ("OOPs basic to advanced")
from array import *

# practice tasks in OOPS 

class Users :
    def __init__(self , name , email):

        self.name = name 
        self.email = email

    def display_info (self):
        print(f"User : {self.name} | {self.email}")


users =  [ 
Users("afzal", "afzal@ccc.com"),
Users("yasir", "yasir@ccc.com"),
Users("nasir", "nasir@ccc.com"),
Users("nasir", "nasir@ccc.com"),
Users("nasir", "nasir@ccc.com"),
Users("nasir", "nasir@ccc.com"),
Users("nasir", "nasir@ccc.com"),
 ]

for usr in users:
    usr.display_info()
         