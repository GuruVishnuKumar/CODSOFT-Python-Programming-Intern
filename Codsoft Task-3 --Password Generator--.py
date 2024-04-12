import random
import string
def generator_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password
print("-----PASSWORD GENERATOR-----\n")
while(True):
    try:
        length=int(input("Enter The Password Lenght -->"))
        if(length<=0):
            print("...The Value Must Greater Than 0\n")
        else:
            password=generator_password(length)
            print("Generated Password ==>",password)
            break
    except ValueError:
        print("Invalid..Please Enter A Valid Integer...\n") 
