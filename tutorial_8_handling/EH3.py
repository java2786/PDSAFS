# write python function to verify if email is valid or not
# only gmail ids are valid

def verifyEmail(email):
    if(email.endswith('@gmail.com')==False):
        raise RuntimeError("Not gmail id")
    elif(" " in email):
        raise RuntimeError("Space found")
    elif(email.count("@")>1):
        raise RuntimeError("Multiple '@' found")
    else:
        return True

my_email = "java@kumar.arun@gmail.com"
try:
    print(verifyEmail(my_email))
except RuntimeError as re: 
    print("Error found",re)