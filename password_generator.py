import random
#Define a function to generate random password
def password_generate(length):
    #create a list for password generation
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567!@#$%^&*"
    #genearte the password 
    password = "".join(random.choice(characters) for _ in range(length))
    return password
#Get the user input from the user
lenght = int(input("How do dou you want your password to be? "))
password = password_generate(lenght)
print("Your password is : " + password)