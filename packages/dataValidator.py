import re

def Validator(num,email):
    mobile_pattren = "^[06789][0-9]{9}$"
    email_pattren = "^[a-z0-9][a-z0-9._]{4,13}[a-z0-9][@][a-z0-9.]{3,18}[a-z]{2,4}"
    if(re.match(mobile_pattren, num)):
        if(re.match(email_pattren,email)):
            return "is valid"
        else:
            return "email is invalid"
    else:
        return "mobile is invalid"

num = input()

email = input()
       
Validator(num,email)