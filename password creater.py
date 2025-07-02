import string
import random




def password():
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    pas=int(input("Enter Password length: "))
    random.shuffle(s)
    pas=("".join(s[0:pas]))
    print(pas)


password()