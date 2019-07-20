# need to check if the email website is live  

import re
import string

def validate_email(email):
    if len(email)>7:
        if re.match(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email) != None:
            return 1
        else:
            return 0
    else:
        return 0
    
#print(validate_email(input("input your email please:")))



def validate_password_strength(password):
    errors = list()
    upper = any(c in string.ascii_uppercase for c in password)
    lower = any(c in string.ascii_lowercase for c in password)
    number = any(c in string.digits for c in password)
    # benign part
    if len(password) < 6:
        errors.append("Your password must be at least 6 characters long")
    if not (upper and lower and number):
        errors.append("Your password must contain at least one uppercase letter, one lowercase letter, and one number")
    else:
        errors.append("Thank you for join, happy reading!")
    return errors[0]

    '''
    if pw.lower() in (email.lower(), username.lower()):
        errors.append("Your password must not be the same as your username or email address")
    '''

    '''
    # evil part - user the registered email & password to try to login other websites and feedback the result...
    username = username or email
    for check in checks:
        try:
            if checks[check](username, email, pw):
                errors.append("Your password must not be the same as your {} password".format(check))
        except:
            pass
    return errors
    '''

print(validate_password_strength(input("input your password please:")))
