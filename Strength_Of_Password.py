import re

def password_strength(password):
    if len(password)<8:
        print("Password is too short")
        
        
    elif not re.search("[a-z]",password):
        print("Password should have at least one uppercase letter")
        
    elif not re.ssearch("[0-9]",password):
        print("Password should have at least one digit")
        
    elif not re.search("[!@#$%^&*()>>?\":{}/<>]",password):
        print("Password should have at least one special charchter")
        
    else:
        print("Password is strong")
        
        
user_password=input("Enter a password to check its strength:")
password_strength(user_password)
        
